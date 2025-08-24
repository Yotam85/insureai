# estimate/tasks.py
from __future__ import annotations

import asyncio, base64, decimal, io, json, logging, re
from typing import Any, Dict, List, Tuple

from celery import shared_task
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .models import EstimateJob, EstimateResult
from .pdf_export import export_estimate_pdf_bytes

# unified agent kit
from estimate.agentkit.insurance_agents import (
    build_insurance_agents,   # triage + specialists
    build_run_config,         # model cfg
    build_input_messages,     # input_text + N images
)
from agents import Runner

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# ---------- helpers ----------

def _extract_json(text: str) -> Dict[str, Any] | None:
    """
    Accepts raw model output. Handles:
      - pure JSON
      - fenced blocks ```json ... ```
      - best-effort { ... } span extraction
    """
    if not isinstance(text, str):
        return None
    # try plain JSON first
    try:
        return json.loads(text)
    except Exception:
        pass

    # fenced ```json ... ```
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S | re.I)
    if m:
        try:
            return json.loads(m.group(1))
        except Exception:
            pass

    # fallback: first {...} to last {...}
    try:
        i, j = text.find("{"), text.rfind("}")
        if i != -1 and j != -1 and j > i:
            return json.loads(text[i : j + 1])
    except Exception:
        pass
    return None


def _build_user_text(job: EstimateJob) -> str:
    """
    Base prompt + user fields (always include BOTH: base guidance AND user-supplied instructions).
    """
    base = (
        "You're a public adjuster. Write a precise estimate from the attached damage images. "
        "Decide per item whether to repair or replace (never both). Use the knowledge base. "
        "Return ONLY raw JSON that matches the unified schema (no markdown fences)."
    )
    parts = [base]
    if job.instructions:
        parts.append(f"User instructions: {job.instructions}")
    if job.damage_type:
        parts.append(f"Peril hint: {job.damage_type}")
    if job.property_type:
        parts.append(f"Property type: {job.property_type}")
    return "\n".join(parts)


def _collect_upload_data_uris(job: EstimateJob) -> Tuple[List[str], List[str]]:
    """
    Build data-URIs for all uploads. Images → base64 data:image/*.
    PDFs are already handled elsewhere in your codebase; include if you need.
    """
    data_uris: List[str] = []
    sent_from: List[str] = []

    for up in job.uploads.all():
        if up.mime.startswith("image/"):
            data = up.file.read()
            b64 = base64.b64encode(data).decode("utf-8")
            data_uris.append(f"data:{up.mime};base64,{b64}")
            sent_from.append(f"{up.id}:{up.file.name}")
        # If you want to support PDF-to-images here, add that logic back.

    # sample log to prove we did send image data
    if data_uris:
        log.info("Sample data URI head: %s", data_uris[0][:80] + "…")
    return data_uris, sent_from


def _normalize_for_premium(payload: Any) -> int:
    """
    Count items for a simple premium heuristic, robust to different shapes.
    """
    try:
        if isinstance(payload, str):
            payload = json.loads(payload)
    except Exception:
        return 1

    if not isinstance(payload, dict):
        return 1

    if isinstance(payload.get("items"), list):
        return max(1, len(payload["items"]))

    if isinstance(payload.get("sections"), list):
        total = 0
        for s in payload["sections"]:
            if isinstance(s, dict) and isinstance(s.get("items"), list):
                total += len(s["items"])
        return max(1, total)

    return 1


# ---------- main task ----------

@shared_task(bind=True, max_retries=3)
def run_estimate(self, job_id: int) -> None:
    """
    Agentic version:
    - build triage + specialists via build_insurance_agents()
    - feed images
    - await Runner.run(...)
    - save JSON, premium, and a rendered PDF
    """
    # 0) Fetch job
    job: EstimateJob = (
        EstimateJob.objects
        .select_related("owner")
        .prefetch_related("uploads")
        .get(pk=job_id)
    )

    # 1) Gather images → data URIs
    data_uris, sent_from = _collect_upload_data_uris(job)
    log.info(
        "Job %s – sending %d image block(s) to Agents:\n%s",
        job.pk, len(data_uris),
        "\n".join(f" • {p}" for p in sent_from) or " • <none>",
    )
    if not data_uris:
        log.warning("Job %s – no uploads found; proceeding without images", job.pk)

    # 2) Build agents + run config
    triage_agent, *_ = build_insurance_agents()
    run_cfg = build_run_config()

    # 3) Build input (text + images)
    user_text = _build_user_text(job)
    input_messages = build_input_messages(user_text, data_uris)

    # 4) Run agent graph
    try:
        result = asyncio.run(
            Runner.run(
                triage_agent,
                input=input_messages,
                run_config=run_cfg,
            )
        )
    except Exception:
        log.exception("Agent run failed for job %s", job_id)
        job.status = "FAILED"
        job.save(update_fields=["status"])
        raise

    # 5) Extract payload (robust to fenced JSON)
    final_output = getattr(result, "final_output", None)
    if isinstance(final_output, dict):
        payload = final_output
    elif isinstance(final_output, str):
        payload = _extract_json(final_output) or {}
    else:
        payload = {}

    log.info("RAW agent payload for job %s:\n%s", job_id, json.dumps(payload, indent=2, default=str))

    # 6) Compute premium (very simple heuristic)
    count = _normalize_for_premium(payload)
    premium = decimal.Decimal("0.8") * decimal.Decimal(count)

    # 7) Render PDF (don’t block saving if rendering fails)
    pdf_saved_path = None
    try:
        pdf_bytes = export_estimate_pdf_bytes(payload)
        filename  = f"estimates/job-{job.id}.pdf"
        pdf_saved_path = default_storage.save(filename, ContentFile(pdf_bytes))
    except Exception:
        log.exception("Failed to render/save PDF for job %s", job.id)

    # 8) Persist result — IMPORTANT: carry owner & guest_key
    res = EstimateResult.objects.create(
        job=job,
        owner=job.owner,          # FK to user (nullable)
        guest_key=job.guest_key,  # CharField (nullable/blank)
        raw_json=payload,
        premium=premium,
        pdf_file=pdf_saved_path or None,
    )

    job.status = "DONE"
    job.save(update_fields=["status"])
    log.info("✅ Saved EstimateResult for job %s (premium=%s, pdf=%s)",
             job.id, premium, (res.pdf_file.url if res.pdf_file else None))


