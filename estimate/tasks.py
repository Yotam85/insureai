# estimate/tasks.py
from __future__ import annotations

import os
import asyncio
import base64
import decimal
import json
import logging
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from celery import shared_task
from django.utils import timezone
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .models import EstimateJob, EstimateResult
from .pdf_export import export_estimate_pdf_bytes
from django.utils import timezone

from estimate.agentkit.insurance_agents import (
    build_agent,          # pick one by job.agent_kind (or triage)
    build_run_config,     # pass to Runner.run(...)
    build_input_messages, # input_text + N images
)
from agents import Runner
from estimate.agentkit.inventory_agent import (
    build_inventory_agent as build_inv_agent,
    build_run_config as build_inv_run_config,
    build_inventory_message,
)

try:
    import cv2  # type: ignore
    try:
        cv2.setNumThreads(0)
    except Exception:
        pass
    try:
        cv2.ocl.setUseOpenCL(False)
    except Exception:
        pass
except Exception:
    cv2 = None


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

VIDEO_SAMPLE_EVERY_N = int(os.getenv("ESTIMATE_VIDEO_SAMPLE_EVERY", "25"))
VIDEO_MAX_FRAMES = int(os.getenv("ESTIMATE_VIDEO_MAX_FRAMES", "80"))
VIDEO_RESIZE_MAX = int(os.getenv("ESTIMATE_VIDEO_RESIZE_MAX", "1280"))
VIDEO_JPEG_QUALITY = int(os.getenv("ESTIMATE_VIDEO_JPEG_QUALITY", "80"))

# Ensure an event loop policy exists for worker main threads (Py3.13/Celery)
try:
    asyncio.get_event_loop()
except RuntimeError:
    try:
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    except Exception:
        pass

# ---------------- JSON helpers ----------------

JSON_FENCE_RE = re.compile(r"```(?:json)?\s*([\s\S]+?)\s*```", re.IGNORECASE)


def _extract_json(text_or_bytes: Any) -> Optional[Any]:
    """
    Robust JSON extractor:
      - Accepts dict/list (passes through)
      - Accepts bytes (decodes utf-8)
      - Accepts plain JSON string (object or array)
      - Accepts fenced ```json ... ``` blocks
      - Best-effort brace/bracket scan
    Returns Python obj (dict/list/whatever) or None.
    """
    if isinstance(text_or_bytes, (dict, list)):
        return text_or_bytes

    if isinstance(text_or_bytes, (bytes, bytearray)):
        try:
            text = text_or_bytes.decode("utf-8", errors="replace")
        except Exception:
            return None
    else:
        text = str(text_or_bytes) if text_or_bytes is not None else ""

    text = text.strip()
    if not text:
        return None

    # 1) direct JSON
    try:
        return json.loads(text)
    except Exception:
        pass

    # 2) fenced block
    m = JSON_FENCE_RE.search(text)
    if m:
        candidate = m.group(1).strip()
        try:
            return json.loads(candidate)
        except Exception:
            pass

    # 3) best-effort span search
    def _span(s: str, open_ch: str, close_ch: str) -> Optional[Tuple[int, int]]:
        i, j = s.find(open_ch), s.rfind(close_ch)
        if i != -1 and j != -1 and j > i:
            return (i, j + 1)
        return None

    brace = _span(text, "{", "}")
    bracket = _span(text, "[", "]")
    span = brace if brace and (not bracket or (brace[1] - brace[0]) >= (bracket[1] - bracket[0])) else bracket
    if span:
        candidate = text[span[0]:span[1]]
        try:
            return json.loads(candidate)
        except Exception:
            pass

    return None


def _encode_frame_b64(frame, *, resize_max: Optional[int] = VIDEO_RESIZE_MAX, jpeg_quality: int = VIDEO_JPEG_QUALITY) -> str:
    if cv2 is None:
        raise RuntimeError("OpenCV (cv2) is required for video processing but is not installed")
    if frame is None:
        raise ValueError("Empty video frame")
    h, w = frame.shape[:2]
    if resize_max and max(h, w) > resize_max:
        scale = resize_max / max(h, w)
        frame = cv2.resize(frame, (max(1, int(w * scale)), max(1, int(h * scale))), interpolation=cv2.INTER_AREA)
    ok, buf = cv2.imencode(
        ".jpg",
        frame,
        [int(cv2.IMWRITE_JPEG_QUALITY), int(jpeg_quality)],
    )
    if not ok:
        raise RuntimeError("Failed to encode video frame as JPEG")
    return base64.b64encode(buf).decode("utf-8")


def _video_to_base64_frames(
    path: str | Path,
    *,
    sample_every_n: int = VIDEO_SAMPLE_EVERY_N,
    max_frames: int = VIDEO_MAX_FRAMES,
    resize_max: Optional[int] = VIDEO_RESIZE_MAX,
    jpeg_quality: int = VIDEO_JPEG_QUALITY,
) -> List[str]:
    frames: List[str] = []
    sample_every_n = max(1, sample_every_n)
    max_frames = max(1, max_frames)

    ffmpeg_bin = shutil.which("ffmpeg")
    if ffmpeg_bin:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_pattern = str(Path(tmpdir) / "frame_%05d.jpg")
            vf_filters: List[str] = [f"select=not(mod(n\,{sample_every_n}))"]
            if resize_max:
                vf_filters.append(f"scale='min({resize_max},iw)':-2")
            vf = ",".join(vf_filters)
            qscale = "2"
            try:
                proc = subprocess.run(
                    [
                        ffmpeg_bin,
                        "-nostdin",
                        "-hide_banner",
                        "-loglevel",
                        "error",
                        "-i",
                        str(path),
                        "-vf",
                        vf,
                        "-vsync",
                        "vfr",
                        "-frames:v",
                        str(max_frames),
                        "-q:v",
                        qscale,
                        output_pattern,
                    ],
                    check=False,
                )
                if proc.returncode == 0:
                    for fp in sorted(Path(tmpdir).glob("frame_*.jpg")):
                        try:
                            frames.append(base64.b64encode(fp.read_bytes()).decode("utf-8"))
                        except Exception:
                            log.exception("Failed reading ffmpeg frame %s", fp)
                    if frames:
                        return frames[:max_frames]
                else:
                    log.warning("ffmpeg exited with code %s while processing %s", proc.returncode, path)
            except FileNotFoundError:
                pass
            except Exception:
                log.exception("ffmpeg failed to extract frames from %s", path)

    if cv2 is None:
        log.warning("Video upload provided but neither ffmpeg nor OpenCV usable; skipping %s", path)
        return frames

    p = str(Path(path).expanduser())
    cap = cv2.VideoCapture(p)
    if not cap.isOpened():
        log.warning("Could not open video %s", p)
        return frames

    idx = 0
    try:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            if idx % sample_every_n == 0:
                try:
                    frames.append(_encode_frame_b64(frame, resize_max=resize_max, jpeg_quality=jpeg_quality))
                except Exception:
                    log.exception("Failed encoding frame %s from %s", idx, p)
                if len(frames) >= max_frames:
                    break
            idx += 1
    finally:
        cap.release()

    return frames


def _safe_update(model_obj, fields: List[str]) -> None:
    """Save only fields that actually exist on the model (guards mixed schemas)."""
    valid = [f for f in fields if hasattr(model_obj, f)]
    if valid:
        model_obj.save(update_fields=valid)


def _coerce_payload_from_result(result: Any) -> Tuple[Any, str]:
    """
    Try multiple places to get JSON/text out of RunResult.
    Returns (payload, raw_text_used_for_fallback).
    """
    # 1) final_output
    fo = getattr(result, "final_output", None)
    payload = _extract_json(fo)
    if payload is not None:
        return payload, str(fo) if isinstance(fo, str) else ""

    # 2) other common attrs
    for attr in ("final_output_text", "text", "message", "content"):
        val = getattr(result, attr, None)
        payload = _extract_json(val)
        if payload is not None:
            return payload, str(val) if isinstance(val, str) else ""

    # 3) scan collections
    texts: List[str] = []

    def _maybe_collect(obj: Any):
        if isinstance(obj, dict):
            if "text" in obj and isinstance(obj["text"], str):
                texts.append(obj["text"])
            elif "content" in obj and isinstance(obj["content"], str):
                texts.append(obj["content"])
        elif isinstance(obj, str):
            texts.append(obj)

    for list_attr in ("new_items", "new_outputs", "items", "outputs"):
        seq = getattr(result, list_attr, None)
        if isinstance(seq, (list, tuple)):
            for it in seq:
                _maybe_collect(it)

    if texts:
        combined = "\n".join(t for t in texts if t)
        payload = _extract_json(combined)
        if payload is not None:
            return payload, combined

    return {}, ""


# --------------- normalization helpers ------------------

def _normalize_items(seq: Any) -> List[Dict[str, Any]]:
    """
    Coerce arbitrary item dicts into the unified schema your PDF/HTML expect:
    id, line_items, QUANTITY, UNIT_PRICE, TAX, TOTAL_PRICE, unit_code, category, Details, ...
    """
    items: List[Dict[str, Any]] = []
    if not isinstance(seq, (list, tuple)):
        return items

    def _f(v: Any, default: float = 0.0) -> float:
        try:
            return float(v)
        except Exception:
            return default

    for idx, it in enumerate(seq, 1):
        if not isinstance(it, dict):
            continue
        qty  = _f(it.get("QUANTITY") or it.get("quantity") or it.get("qty") or 1)
        unit = (it.get("unit_code") or it.get("unit") or "EA") or "EA"
        up   = _f(it.get("UNIT_PRICE") or it.get("unit_rcv") or it.get("unit_price") or 0)
        tax  = _f(it.get("TAX") or it.get("tax") or 0)
        tot  = _f(it.get("TOTAL_PRICE") or it.get("total_rcv") or (qty * up + tax))

        items.append({
            "id":          it.get("id", idx),
            "line_items":  it.get("line_items") or it.get("description") or it.get("item") or "",
            "QUANTITY":    qty,
            "UNIT_PRICE":  up,
            "TAX":         tax,
            "TOTAL_PRICE": tot,
            "unit_code":   unit,
            "category":    it.get("category") or "General",
            "Details":     it.get("Details") or it.get("notes") or "",
            "tags":        it.get("tags") or [],
            "source":      it.get("source") or {},
            "metadata":    {k: v for k, v in it.items() if k not in {
                "id","line_items","description","item","quantity","qty","QUANTITY","UNIT_PRICE",
                "unit_price","unit_rcv","TAX","tax","TOTAL_PRICE","total_rcv","unit","unit_code",
                "category","Details","notes","tags","source"
            }},
        })
    return items


def _to_safe_payload(payload: Any) -> Dict[str, Any]:
    """
    Coerce model output into the shape serializers/pdf_export expect:
    {
      items: [normalized items],
      summary: { total_project_cost, estimate_reasoning, future_actions },
      currency: "USD",
      ... (carry through helpful fields like peril/property_type/etc)
    }
    """
    if isinstance(payload, list):
        norm = _normalize_items(payload)
        total = sum(float(i.get("TOTAL_PRICE") or 0) for i in norm)
        return {
            "items": norm,
            "summary": {
                "total_project_cost": float(total),
                "estimate_reasoning": "",
                "future_actions": [],
            },
            "currency": "USD",
        }

    if isinstance(payload, dict):
        p = dict(payload)  # shallow copy

        items_raw = (
            p.get("items")
            or p.get("line_items")
            or (p.get("estimate") or {}).get("items")
            or []
        )
        if not items_raw and isinstance(p.get("sections"), list):
            flat: List[Dict[str, Any]] = []
            for s in p["sections"]:
                if isinstance(s, dict) and isinstance(s.get("items"), list):
                    flat.extend(s["items"])
            items_raw = flat

        norm = _normalize_items(items_raw)

        # summary could be string/missing
        summary = p.get("summary")
        if not isinstance(summary, dict):
            summary = {
                "estimate_reasoning": "" if summary in (None, "", {}) else str(summary),
                "future_actions": [],
            }

        # compute total if missing/bad
        try:
            _ = float(summary.get("total_project_cost"))
            total_ok = True
        except Exception:
            total_ok = False
        if not total_ok:
            summary["total_project_cost"] = float(sum(float(i.get("TOTAL_PRICE") or 0) for i in norm))

        out: Dict[str, Any] = {
            "items": norm,
            "summary": summary,
            "currency": p.get("currency") or "USD",
        }
        for k in ("peril", "property_type", "assumptions", "totals", "version", "generated_at", "workflow", "location"):
            if k in p:
                out[k] = p[k]
        return out

    return {
        "items": [],
        "summary": {"total_project_cost": 0.0, "estimate_reasoning": "", "future_actions": []},
        "currency": "USD",
    }


# ---------------- Inventory agent helpers ----------------

def generate_inventory_suggestion_from_items(items: List[Dict[str, Any]], *, currency: str = "USD") -> List[Dict[str, Any]]:
    """
    Run the inventory agent synchronously on normalized estimate items and return a list of
    {name, quantity, unit, unit_cost} dicts. Never raises; returns [] on failure.
    """
    try:
        agent = build_inv_agent(currency=currency)
        run_cfg = build_inv_run_config(os.environ.get("OPENAI_MODEL"))
        try:
            run_cfg.workflow_name = "InventorySuggestion"
        except Exception:
            pass

        # Keep the payload compact: only fields the user cares about
        compact_items = []
        for it in items or []:
            if isinstance(it, dict):
                compact_items.append({
                    "description": it.get("line_items") or it.get("description") or "",
                    "quantity": it.get("QUANTITY") or it.get("quantity") or 0,
                    "unit": it.get("unit_code") or it.get("unit") or "EA",
                })

        messages = build_inventory_message({"items": compact_items}, currency=currency)

        # Ensure an event loop exists for Runner.run_sync in request threads
        created_loop = None
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            created_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(created_loop)

        try:
            result = Runner.run_sync(agent, messages, run_config=run_cfg, max_turns=4)
        finally:
            if created_loop is not None:
                try:
                    created_loop.close()
                except Exception:
                    pass
                asyncio.set_event_loop(None)

        payload = _extract_json(getattr(result, "final_output", None)) or _extract_json(getattr(result, "text", "")) or {}
        inv = (payload or {}).get("inventory")
        if isinstance(inv, list):
            cleaned: List[Dict[str, Any]] = []
            for row in inv:
                if not isinstance(row, dict):
                    continue
                try:
                    cleaned.append({
                        "name": str(row.get("name", ""))[:200],
                        "quantity": float(row.get("quantity", 0) or 0),
                        "unit": str(row.get("unit", "")).upper()[:16],
                        "unit_cost": float(row.get("unit_cost", 0) or 0),
                    })
                except Exception:
                    continue
            return cleaned
    except Exception:
        log.exception("Inventory suggestion generation failed")
    return []


@shared_task(bind=True, max_retries=2)
def run_inventory_suggestion(self, result_id: int) -> List[Dict[str, Any]]:
    """
    Celery wrapper to generate inventory suggestions for a given EstimateResult.
    Returns the suggested list (not persisted).
    """
    try:
        result = EstimateResult.objects.select_related("job").get(pk=result_id)
    except EstimateResult.DoesNotExist:
        return []

    # Mark running (only if fields exist)
    try:
        if hasattr(result, "inventory_status"):
            result.inventory_status = "RUNNING"
        if hasattr(result, "inventory_task_id"):
            result.inventory_task_id = getattr(self.request, "id", None)
        _safe_update(result, ["inventory_status", "inventory_task_id"])
    except Exception:
        pass

    data = result.raw_json or {}
    items: List[Dict[str, Any]] = []
    currency = "USD"
    if isinstance(data, dict):
        currency = data.get("currency") or "USD"
        if isinstance(data.get("items"), list):
            items = _normalize_items(data["items"])  # normalize again just in case

    inv = generate_inventory_suggestion_from_items(items, currency=currency)
    try:
        # Persist suggestion to result for better UX
        result.inventory = inv
        if hasattr(result, "inventory_status"):
            result.inventory_status = "DONE"
        if hasattr(result, "inventory_updated"):
            result.inventory_updated = timezone.now()
        _safe_update(result, ["inventory", "inventory_status", "inventory_updated"])
        try:
            total = 0.0
            for r in inv or []:
                try:
                    total += float(r.get("quantity", 0) or 0) * float(r.get("unit_cost", 0) or 0)
                except Exception:
                    pass
            job_id = getattr(result, "job_id", None)
            claim  = getattr(getattr(result, "job", None), "claim_number", "") or ""
            log.info("INVENTORY_READY job=%s claim=%s rows=%s total=%s", job_id, claim, len(inv or []), total)
        except Exception:
            pass
    except Exception:
        log.exception("Failed saving inventory suggestion for result %s", result_id)
        try:
            if hasattr(result, "inventory_status"):
                result.inventory_status = "FAILED"
            if hasattr(result, "inventory_updated"):
                result.inventory_updated = timezone.now()
            _safe_update(result, ["inventory_status", "inventory_updated"])
        except Exception:
            pass
    return inv


@shared_task(bind=True, max_retries=2)
def run_inventory_suggestion_from_items(self, items: List[Dict[str, Any]], currency: str = "USD") -> List[Dict[str, Any]]:
    """Celery wrapper to generate inventory from provided items (no DB lookup)."""
    return generate_inventory_suggestion_from_items(items, currency=currency)


@shared_task(bind=True, max_retries=2)
def run_inventory_suggestion_with_override(self, result_id: int, items: List[Dict[str, Any]], currency: str = "USD") -> List[Dict[str, Any]]:
    """Generate inventory for a specific result using provided items; persist to DB."""
    try:
        result = EstimateResult.objects.get(pk=result_id)
    except EstimateResult.DoesNotExist:
        return []
    inv = generate_inventory_suggestion_from_items(items or [], currency=currency)
    try:
        result.inventory = inv
        if hasattr(result, "inventory_status"):
            result.inventory_status = "DONE"
        if hasattr(result, "inventory_updated"):
            result.inventory_updated = timezone.now()
        _safe_update(result, ["inventory", "inventory_status", "inventory_updated"])
        try:
            total = 0.0
            for r in inv or []:
                try:
                    total += float(r.get("quantity", 0) or 0) * float(r.get("unit_cost", 0) or 0)
                except Exception:
                    pass
            job_id = getattr(result, "job_id", None)
            claim  = getattr(getattr(result, "job", None), "claim_number", "") or ""
            log.info("INVENTORY_READY job=%s claim=%s rows=%s total=%s", job_id, claim, len(inv or []), total)
        except Exception:
            pass
    except Exception:
        log.exception("Failed saving override inventory for result %s", result_id)
        try:
            if hasattr(result, "inventory_status"):
                result.inventory_status = "FAILED"
            if hasattr(result, "inventory_updated"):
                result.inventory_updated = timezone.now()
            _safe_update(result, ["inventory_status", "inventory_updated"])
        except Exception:
            pass
    return inv


# --------------- misc helpers ------------------

def _build_user_text(job: EstimateJob) -> str:
    base = (
        "You're a senior apprisel / construction estimator. "
        "Carfully analyse my image(s) and create an estimate according your knowledge. some users may include floor plans and existing takeoff plans to be aware of that."
        "Return ONLY raw JSON matching the role schema."
    )
    parts = [base]
    if job.instructions:
        parts.append(f"User instructions: {job.instructions}")
    if job.property_type:
        parts.append(f"Property type: {job.property_type}")
    if getattr(job, "work_grade", None):
        parts.append(f"Work grade: {job.work_grade}")
    return "\n".join(parts)


def _collect_upload_data_uris(job: EstimateJob) -> Tuple[List[str], List[str]]:
    data_uris: List[str] = []
    sent_from: List[str] = []
    for up in job.uploads.all():
        mime = (up.mime or "").lower() if isinstance(up.mime, str) else ""
        if mime.startswith("image/"):
            try:
                with up.file.open("rb") as f:
                    raw = f.read()
                b64 = base64.b64encode(raw).decode("utf-8")
                data_uris.append(f"data:{up.mime};base64,{b64}")
                sent_from.append(f"{up.id}:{up.file.name} ({len(raw)} bytes)")
            except Exception:
                log.exception("Failed reading upload %s for job %s", up.pk, job.pk)
        elif mime.startswith("video/"):
            path = getattr(getattr(up, "file", None), "path", None)
            temp_path = None
            if not path:
                suffix = Path(up.file.name or "video").suffix or ".mp4"
                try:
                    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
                        temp_path = tmp.name
                        up.file.open("rb")
                        try:
                            for chunk in up.file.chunks():
                                tmp.write(chunk)
                        finally:
                            up.file.close()
                    path = temp_path
                except Exception:
                    log.exception("Failed preparing temp file for video upload %s", up.pk)
                    if temp_path and os.path.exists(temp_path):
                        os.unlink(temp_path)
                    continue
            try:
                frames_b64 = _video_to_base64_frames(path)
                for idx, b64 in enumerate(frames_b64):
                    data_uris.append(f"data:image/jpeg;base64,{b64}")
                    sent_from.append(f"{up.id}:{up.file.name} frame {idx}")
                if frames_b64:
                    log.info(
                        "Sampled %d frame(s) from video %s for job %s",
                        len(frames_b64), up.pk, job.pk
                    )
            except Exception:
                log.exception("Failed extracting frames from video upload %s for job %s", up.pk, job.pk)
            finally:
                if temp_path and os.path.exists(temp_path):
                    os.unlink(temp_path)
    if data_uris:
        head = data_uris[0][:80] + "…"
        log.info("Prepared %d image block(s) for job %s. Sample head: %s", len(data_uris), job.pk, head)
        log.info("Sending images:\n%s", "\n".join(f" • {p}" for p in sent_from))
    return data_uris, sent_from


def _to_decimal(value: Any) -> decimal.Decimal:
    try:
        if isinstance(value, decimal.Decimal):
            return value
        if value in (None, ""):
            return decimal.Decimal("0")
        return decimal.Decimal(str(value))
    except Exception:
        return decimal.Decimal("0")


def _compute_total_cost(payload: Any) -> decimal.Decimal:
    """Best-effort total extraction from agent payload."""
    try:
        if isinstance(payload, str):
            payload = json.loads(payload)
    except Exception:
        return decimal.Decimal("0")

    if not isinstance(payload, dict):
        return decimal.Decimal("0")

    summary = payload.get("summary")
    if isinstance(summary, dict):
        total_val = _to_decimal(summary.get("total_project_cost"))
        if total_val > 0:
            return total_val

    total = decimal.Decimal("0")
    items = payload.get("items")
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                total += _to_decimal(
                    item.get("TOTAL_PRICE")
                    or item.get("total_price")
                    or item.get("total")
                    or item.get("total_rcv")
                )
    elif isinstance(payload.get("sections"), list):
        for section in payload["sections"]:
            if isinstance(section, dict) and isinstance(section.get("items"), list):
                for item in section["items"]:
                    if isinstance(item, dict):
                        total += _to_decimal(
                            item.get("TOTAL_PRICE")
                            or item.get("total_price")
                            or item.get("total")
                            or item.get("total_rcv")
                        )

    return total


# --------------- the task ------------------

@shared_task(bind=True, max_retries=3)
def run_estimate(self, job_id: int) -> None:
    """
    Runs the unified agent pipeline and persists EstimateResult.
    Uses Runner.run_sync per SDK docs; includes safe (string) trace metadata.
    """
    # 0) Load job
    job: EstimateJob = (
        EstimateJob.objects
        .select_related("owner")
        .prefetch_related("uploads")
        .get(pk=job_id)
    )

    log.info(
        "🔧 run_estimate started for job %s (owner=%s, guest=%s, kind=%s)",
        job.pk, getattr(job.owner, "id", None), job.guest_key, getattr(job, "agent_kind", None)
    )

    # 1) Gather uploads as data URIs (images only)
    data_uris, sent_from = _collect_upload_data_uris(job)
    if not sent_from:
        log.info("No image uploads found for job %s", job.pk)

    # 2) Build agent + run_config
    try:
        # Build agent with contextual settings from job/project
        settings = {
            "currency": "USD",
            "property_type": job.property_type or "",
            "work_grade": getattr(job, "work_grade", "") or "",
            "location": getattr(getattr(job, "project", None), "zip", "") or "",
        }
        agent = build_agent((job.agent_kind or "").strip() or None, settings=settings)

        run_cfg = build_run_config(os.environ.get("OPENAI_MODEL"))

        # Tracing (strings only to appease tracer)
        try:
            run_cfg.workflow_name = "EstimateJob"
            run_cfg.group_id = f"job-{job.id}"
            run_cfg.trace_metadata = {
                "job_id": str(job.id),
                "agent_kind": str(getattr(job, "agent_kind", "") or ""),
                "user_id": str(getattr(job, "owner_id", "") or ""),
                "property_type": str(job.property_type or ""),
                "work_grade": str(getattr(job, "work_grade", "") or ""),
                "location": str(getattr(getattr(job, "project", None), "zip", "") or ""),
            }
        except Exception:
            pass
    except Exception:
        log.exception("Failed to build agents/config for job %s", job_id)
        job.status = "FAILED"
        job.save(update_fields=["status"])
        raise

    # 3) Compose input messages (text + N images)
    user_text = _build_user_text(job)
    input_messages = build_input_messages(user_text, data_uris)

    # 4) Run the agent graph (ensure an asyncio loop exists in this thread)
    created_loop = None
    try:
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            created_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(created_loop)

        result = Runner.run_sync(
            agent,
            input_messages,     # OpenAI Responses API-style inputs
            run_config=run_cfg,
            max_turns=8,        # guard against runaway loops
        )
    except Exception:
        log.exception("Agent run failed for job %s", job_id)
        job.status = "FAILED"
        job.save(update_fields=["status"])
        raise
    finally:
        if created_loop is not None:
            try:
                created_loop.close()
            except Exception:
                pass
            asyncio.set_event_loop(None)

    # 5) Extract payload once (don't overwrite later)
    payload, raw_text = _coerce_payload_from_result(result)
    if (not payload or (isinstance(payload, dict) and not payload)) and raw_text:
        payload = {"_raw_text": raw_text[:8000]}  # keep something for debugging

    safe_payload = _to_safe_payload(payload)

    log.info("RAW agent payload for job %s:\n%s", job_id, json.dumps(payload, indent=2, default=str))

    # 6) Total cost extraction
    total_cost = _compute_total_cost(safe_payload)

    # 8) Persist result — carry owner & guest_key (idempotent on job)
    try:
        res, created = EstimateResult.objects.get_or_create(
            job=job,
            defaults={
                "owner": job.owner,
                "guest_key": job.guest_key,
                "raw_json": safe_payload,
                "total_cost": total_cost,
                "pdf_file": None,
            },
        )
        if not created:
            res.raw_json = safe_payload
            res.total_cost = total_cost
            res.save(update_fields=["raw_json", "total_cost"])
        job.status = "DONE"
        job.save(update_fields=["status"])
        # Compose a concise, greppable line for FE/ops
        try:
            claim = getattr(job, "claim_number", "") or ""
            summary = (safe_payload.get("summary") or {}) if isinstance(safe_payload, dict) else {}
            total  = summary.get("total_project_cost")
            items_n = len(safe_payload.get("items") or []) if isinstance(safe_payload, dict) else None
            log.info(
                "RESULT_READY job=%s claim=%s items=%s total=%s persisted_total=%s",
                job.id, claim, items_n, total, str(total_cost)
            )
        except Exception:
            pass
    except Exception:
        log.exception("Failed to save EstimateResult for job %s", job_id)
        job.status = "FAILED"
        job.save(update_fields=["status"])
        raise
