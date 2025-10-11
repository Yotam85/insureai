"""Heuristic project planning helper used by the AI planning endpoint.

The goal is to take the strongly-typed payload from the frontend, run a
deterministic scheduling heuristic, and return a structure that matches the
expected `AiPlanResponse` contract. The logic is intentionally written so that
it can be swapped out for an LLM agent in the future without touching the
REST surface area.
"""

from __future__ import annotations

from dataclasses import dataclass
import copy
import logging
import math
import re
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Phase heuristics
# ---------------------------------------------------------------------------
PHASE_ORDER: List[str] = [
    "site_prep",
    "demolition",
    "rough_fix",
    "insulation",
    "drywall",
    "prime_paint",
    "flooring_sub",
    "flooring",
    "trim_finish",
    "final_clean",
    "contingency",
]


DEFAULTS: Dict[str, Dict[str, int]] = {
    "site_prep": {"duration": 1, "crew": 1},
    "demolition": {"duration": 1, "crew": 2},
    "rough_fix": {"duration": 1, "crew": 2},
    "insulation": {"duration": 1, "crew": 1},
    "drywall": {"duration": 2, "crew": 2},
    "prime_paint": {"duration": 1, "crew": 1},
    "flooring_sub": {"duration": 1, "crew": 1},
    "flooring": {"duration": 1, "crew": 2},
    "trim_finish": {"duration": 1, "crew": 1},
    "final_clean": {"duration": 1, "crew": 1},
    "contingency": {"duration": 1, "crew": 1},
}


# ---------------------------------------------------------------------------
# Slot helpers
# ---------------------------------------------------------------------------
def normalize_slots(payload: Dict[str, Any], *, min_slots: int = 7, max_slots: int = 120) -> List[Dict[str, Any]]:
    """Normalize the slots array to contain unique ids/labels and ensure a minimum count."""

    raw_slots = payload.get("slots")
    slots: List[Dict[str, Any]] = []
    seen: set[str] = set()

    if isinstance(raw_slots, list):
        for index, raw in enumerate(raw_slots, 1):
            if not isinstance(raw, dict):
                continue
            slot_id = str(raw.get("id") or "").strip()
            if not slot_id:
                slot_id = f"day-{index}"
            base_id = slot_id
            counter = 1
            while slot_id in seen or not slot_id:
                slot_id = f"{base_id or 'day'}-{counter}"
                counter += 1
            seen.add(slot_id)

            slot_label = str(raw.get("label") or "").strip()
            order_val = raw.get("order")
            if isinstance(order_val, int) and order_val > 0:
                order = order_val
            else:
                order = len(slots) + 1
            if not slot_label or slot_label.lower() in {"day", "days"}:
                slot_label = f"Day {order}"

            display = str(raw.get("display") or "").strip()
            if not display:
                display = slot_label

            slots.append({
                "id": slot_id,
                "label": slot_label,
                "order": order,
                "display": display,
            })

    desired = max(min_slots, len(slots))
    if max_slots:
        desired = min(desired, max_slots)

    while len(slots) < desired:
        index = len(slots) + 1
        slot_id = f"day-{index}"
        counter = index
        while slot_id in seen:
            counter += 1
            slot_id = f"day-{counter}"
        seen.add(slot_id)
        label = f"Day {len(slots) + 1}"
        slots.append({
            "id": slot_id,
            "label": label,
            "order": len(slots) + 1,
            "display": label,
        })

    slots.sort(key=lambda slot: slot.get("order") or 0)
    for index, slot in enumerate(slots, 1):
        slot["order"] = index
        label = str(slot.get("label") or "").strip()
        if not label or label.lower() in {"day", "days"}:
            label = f"Day {index}"
        slot["label"] = label
        display = str(slot.get("display") or "").strip()
        if not display:
            display = label
        slot["display"] = display

    payload["slots"] = slots
    return slots


# Phases that can overlap with others when enough crews are available.
PARALLEL_OK: Dict[str, set[str]] = {
    "site_prep": {"demolition", "rough_fix"},
    "demolition": {"site_prep"},
    "prime_paint": set(),
    "final_clean": set(),
}


def infer_phase(task: Dict[str, Any]) -> str:
    """Best-effort phase inference based on category/title cues."""

    category = str((task.get("category") or "").strip().lower())
    title = str((task.get("title") or "").strip().lower())

    cat_map = {
        "site_cleanup": "site_prep",
        "site_service": "site_prep",
        "temporary_storage": "site_prep",
        "waste_management": "site_prep",
        "logistics": "site_prep",
        "demo/hauling": "demolition",
        "demolition": "demolition",
        "labor": "demolition",
        "flooring_demo": "demolition",
        "drywall": "drywall",
        "finish_carpentry": "drywall",
        "insulation": "insulation",
        "painting": "prime_paint",
        "flooring_sub": "flooring_sub",
        "flooring": "flooring",
        "trim": "trim_finish",
        "cleaning": "final_clean",
        "contingency": "contingency",
        "electrical": "rough_fix",
        "site_prep": "site_prep",
    }

    if category in cat_map:
        return cat_map[category]

    if re.search(r"dumpster|container|haul debris|pickup truck|temporary", title):
        return "site_prep"
    if "demo" in title or "tear out" in title or "remove existing" in title:
        return "demolition"
    if "subfloor repair" in title or ("allowance" in title and "electrical" in title):
        return "rough_fix"
    if "insulation" in title:
        return "insulation"
    if "drywall" in title:
        return "drywall"
    if any(word in title for word in ("prime", "paint", "texture", "seal")):
        return "prime_paint"
    if "underlayment" in title:
        return "flooring_sub"
    if any(word in title for word in ("flooring", "vinyl plank", "engineered wood")):
        return "flooring"
    if "baseboard" in title or "trim" in title:
        return "trim_finish"
    if "final clean" in title or "construction - residential" in title:
        return "final_clean"
    if "contingency" in title or "o&p" in title:
        return "contingency"

    return "rough_fix"


def _coerce_positive_int(value: Any, fallback: int) -> int:
    try:
        if value is None:
            raise ValueError
        if isinstance(value, bool):
            raise ValueError
        number = float(value)
        if not math.isfinite(number):
            raise ValueError
        number = int(round(number))
        if number <= 0:
            raise ValueError
        return number
    except Exception:
        return fallback


@dataclass
class STask:
    id: str
    phase: str
    duration: int
    crew: int
    original: Dict[str, Any]


def normalize_task(task: Dict[str, Any]) -> Optional[STask]:
    try:
        task_id = str(task["id"])
    except Exception:
        return None

    phase = infer_phase(task)
    meta = task.get("meta") or {}

    default_duration = DEFAULTS.get(phase, {"duration": 1}).get("duration", 1)
    duration = _coerce_positive_int(meta.get("durationDays"), default_duration)
    crew_default = DEFAULTS.get(phase, {"crew": 1}).get("crew", 1)
    crew = _coerce_positive_int(meta.get("crew") if isinstance(meta, dict) else None, crew_default)

    return STask(
        id=task_id,
        phase=phase,
        duration=max(1, duration),
        crew=max(1, crew),
        original=task,
    )


def keep_existing(timeline: Dict[str, Sequence[str]]) -> Dict[str, List[str]]:
    cleaned: Dict[str, List[str]] = {}
    for key, values in (timeline or {}).items():
        seen: set[str] = set()
        cleaned[key] = []
        for value in values or []:
            as_str = str(value)
            if as_str in seen:
                continue
            cleaned[key].append(as_str)
            seen.add(as_str)
    return cleaned


def scheduled_ids(timeline: Dict[str, Sequence[str]]) -> set[str]:
    result: set[str] = set()
    for values in timeline.values():
        for value in values or []:
            result.add(str(value))
    return result


def can_overlap(phase_a: str, phase_b: str) -> bool:
    if phase_a == phase_b:
        return False
    a = PARALLEL_OK.get(phase_a, set())
    b = PARALLEL_OK.get(phase_b, set())
    return phase_b in a or phase_a in b


def phase_index(phase: str) -> int:
    try:
        return PHASE_ORDER.index(phase)
    except ValueError:
        return len(PHASE_ORDER) + 99


def day_phase_floor(tasks: Iterable[STask]) -> int:
    phases = [phase_index(t.phase) for t in tasks]
    return max(phases) if phases else -1


def fits_today(existing: List[STask], task: STask, crews_used: int, max_crews: int) -> bool:
    if crews_used + task.crew > max_crews:
        return False
    if not existing:
        return True
    return all(can_overlap(task.phase, other.phase) for other in existing)


def build_index(tasks: Sequence[STask]) -> Dict[str, STask]:
    return {task.id: task for task in tasks}


def _day_tasks(day: str, occupancy: Dict[str, List[str]], by_id: Dict[str, STask]) -> List[STask]:
    ids = occupancy.get(day, [])
    result: List[STask] = []
    for task_id in ids:
        task = by_id.get(task_id)
        if task:
            result.append(task)
    return result


def plan_project_schedule(
    payload: Dict[str, Any],
    *,
    max_crews_per_day: int = 3,
    lock_existing: bool = True,
) -> Dict[str, Any]:
    """Return an `AiPlanResponse` style dict for the given payload."""

    project_payload = copy.deepcopy(payload or {})

    raw_tasks: List[Dict[str, Any]] = []
    for task in project_payload.get("tasks") or []:
        if not isinstance(task, dict):
            continue
        if "id" not in task:
            continue
        raw_tasks.append(task)

    normalized: List[STask] = [
        norm for norm in (normalize_task(t) for t in raw_tasks) if norm is not None
    ]
    by_id = build_index(normalized)

    slot_defs = normalize_slots(
        project_payload,
        min_slots=max(1, len(normalized)),
    )
    day_keys = [slot["id"] for slot in slot_defs]
    if not day_keys:
        raise ValueError("No planning slots available after normalisation")

    incoming_timeline_raw = keep_existing(project_payload.get("timeline") or {})
    unknown_assignments: List[str] = []
    incoming_timeline: Dict[str, List[str]] = {}
    for slot_id, ids in incoming_timeline_raw.items():
        if slot_id in day_keys:
            incoming_timeline[slot_id] = ids
        else:
            unknown_assignments.extend(ids)

    unscheduled_ids = [str(x) for x in project_payload.get("unscheduledTaskIds") or []]
    unscheduled_ids.extend(unknown_assignments)

    # Occupancy maps each day -> list of task ids that are active that day (for crew capacity).
    occupancy: Dict[str, List[str]] = {key: [] for key in day_keys}
    start_assignments: Dict[str, List[str]] = {key: list(incoming_timeline.get(key, [])) for key in day_keys}

    # Seed occupancy with existing tasks, stretching across their meta duration when possible.
    day_index = {day: idx for idx, day in enumerate(day_keys)}
    for day, ids in start_assignments.items():
        idx = day_index[day]
        for task_id in ids:
            task = by_id.get(task_id)
            occupancy[day].append(task_id)
            if not task:
                continue
            for extra in range(1, task.duration):
                offset = idx + extra
                if offset >= len(day_keys):
                    break
                occupancy[day_keys[offset]].append(task_id)

    already_scheduled = scheduled_ids(start_assignments)

    if lock_existing:
        candidate_ids = [tid for tid in unscheduled_ids if tid in by_id]
    else:
        candidate_ids = [task.id for task in normalized]
        start_assignments = {day: [] for day in day_keys}
        occupancy = {day: [] for day in day_keys}
        already_scheduled = set()

    if not candidate_ids:
        notes = "No unscheduled tasks were provided; existing timeline left unchanged."
        return {
            "timeline": {
                day: [
                    _assignment_payload(task_id, by_id)
                    for task_id in start_assignments.get(day, [])
                ]
                for day in day_keys
                if start_assignments.get(day)
            },
            "unscheduled": unscheduled_ids,
            "notes": notes,
            "slots": slot_defs,
        }

    def sort_key(task: STask) -> Tuple[int, str]:
        return phase_index(task.phase), task.id

    candidates = sorted((by_id[tid] for tid in candidate_ids), key=sort_key)

    placed: set[str] = set()

    def place_block(start_idx: int, task: STask) -> Optional[str]:
        if start_idx + task.duration > len(day_keys):
            return None

        crews_each_day: List[int] = []
        for offset in range(task.duration):
            daykey = day_keys[start_idx + offset]
            todays = _day_tasks(daykey, occupancy, by_id)
            crews_used = sum(item.crew for item in todays)
            if not fits_today(todays, task, crews_used, max_crews_per_day):
                return None
            crews_each_day.append(crews_used)

        start_day = day_keys[start_idx]
        for offset in range(task.duration):
            daykey = day_keys[start_idx + offset]
            occupancy.setdefault(daykey, []).append(task.id)
        start_assignments.setdefault(start_day, []).append(task.id)

        raw_task = by_id[task.id].original
        meta = raw_task.setdefault("meta", {}) if isinstance(raw_task, dict) else {}
        if isinstance(meta, dict):
            meta["startSlot"] = start_day
            meta["startDate"] = start_day
            meta["durationDays"] = task.duration

        placed.add(task.id)
        return start_day

    for task in candidates:
        placed_flag = False
        for start_index, day in enumerate(day_keys):
            if day in start_assignments and task.id in start_assignments[day]:
                placed_flag = True
                break

            todays = _day_tasks(day, occupancy, by_id)
            if todays:
                max_phase_today = day_phase_floor(todays)
                if phase_index(task.phase) < max_phase_today:
                    if not all(can_overlap(task.phase, other.phase) for other in todays):
                        continue
            if place_block(start_index, task):
                placed_flag = True
                break
        if not placed_flag:
            log.debug("Task %s could not be scheduled within available slots", task.id)

    unscheduled_left = list(dict.fromkeys(tid for tid in unscheduled_ids if tid not in placed))

    timeline_payload: Dict[str, List[Dict[str, Any]]] = {}
    for day in day_keys:
        starts = start_assignments.get(day, [])
        if not starts:
            continue
        assignments = [_assignment_payload(task_id, by_id) for task_id in starts]
        if assignments:
            timeline_payload[day] = assignments

    summary = None
    notes = f"Scheduled {len(placed)} of {len(candidate_ids)} pending tasks across {len(day_keys)} slots."
    if unscheduled_left:
        summary = (
            f"Unavailable slots for: {', '.join(unscheduled_left[:5])}"
            + ("…" if len(unscheduled_left) > 5 else "")
        )

    return {
        "timeline": timeline_payload,
        "unscheduled": unscheduled_left,
        "notes": notes,
        "summary": summary,
        "slots": slot_defs,
    }


def _assignment_payload(task_id: str, by_id: Dict[str, STask]) -> Dict[str, Any]:
    task = by_id.get(task_id)
    payload: Dict[str, Any] = {"taskId": task_id}
    if task:
        if task.duration:
            payload["durationDays"] = task.duration
        meta = task.original.get("meta") if isinstance(task.original, dict) else {}
        if isinstance(meta, dict):
            status = meta.get("status")
            if isinstance(status, str) and status.strip():
                payload["status"] = status.strip()
            notes = meta.get("notes")
            if isinstance(notes, str) and notes.strip():
                payload["notes"] = notes.strip()
    return payload
