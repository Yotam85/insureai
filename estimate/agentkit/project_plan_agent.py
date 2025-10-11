"""OpenAI Agent for generating construction project plans."""

from __future__ import annotations

from typing import Any, Dict
import json

from agents import Agent, RunConfig


STRICT_JSON = (
    "Return ONLY raw JSON that exactly matches the schema. "
    "No explanations, backticks, or conversational text."
)


PLAN_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "timeline": {
            "type": "object",
            "additionalProperties": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "taskId": {"type": "string"},
                        "durationDays": {"type": "number", "minimum": 0},
                        "status": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["taskId"],
                    "additionalProperties": False,
                },
            },
        },
        "unscheduled": {
            "type": "array",
            "items": {"type": "string"},
            "uniqueItems": True,
        },
        "notes": {"type": "string"},
        "summary": {"type": "string"},
        "confidence": {
            "type": "object",
            "properties": {
                "rating": {"type": "string", "enum": ["low", "medium", "high"]},
                "rationale": {"type": "string"},
            },
            "required": ["rating", "rationale"],
            "additionalProperties": False,
        },
        "slots": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "label": {"type": "string"},
                    "order": {"type": "integer", "minimum": 1},
                    "display": {"type": "string"},
                },
                "required": ["id", "label"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["timeline", "unscheduled"],
    "additionalProperties": False,
}


def build_plan_agent(*, locale: str = "US") -> Agent:
    """Configure the planning agent with schema instructions."""

    header = {
        "locale": locale,
        "goal": "Allocate work across the provided day slots while keeping dependent trades in order.",
        "crewCapacity": 2,
    }

    instructions = (
        "You are a seasoned construction scheduler planning renovation work for a single property.\n"
        "Given estimate line items with metadata, produce a day-by-day plan using the `slots` array provided in the payload (e.g., `day-1`, `day-2`, …).\n"
        "You plan the full project for the user - he can later modify the results if needed. You can plan it for the days needed for the project. add multiple items a day if you think some tasks can be completed in the same day. you arrange the work to make sense for full 8h work, day by day regardless of weekends. If you see dulolicate estimates that the user might add accedently don't add them to the project and let add it to the [rationale] \n"
        "Respect trade sequencing: demolition must finish before drywall, paint after drywall, flooring only once subfloor and paint are complete, etc.\n"
        "Assume at most 2 crews per day; flag overflow items as unscheduled.\n"
        "Timeline keys MUST match slot ids exactly as provided in the payload.\n"
        "If additional days are required, append new slots (e.g., `day-8`, `day-9`) and include them in the slots array with clear label/display/order values.\n"
        "Return the `slots` array in your response, updating `order` and `display` as needed to reflect the schedule you created.\n"
        f"{STRICT_JSON}\n\n"
        "HEADER CONTEXT (do not rewrite keys, reference as needed):\n"
        f"{json.dumps(header, indent=2)}\n\n"
        "SCHEMA (copy exactly):\n"
        f"{json.dumps(PLAN_SCHEMA, indent=2)}\n\n"
        "Follow these rules:\n"
        "- Use slot ids from the payload as keys (for example `day-1`).\n"
        "- Populate each assignment with reasonable durations; default to 1 if unsure.\n"
        "- Keep unscheduled IDs for items that cannot fit; explain briefly in notes.\n"
        "- Summaries should highlight high-risk trades or missing information in 2 sentences or fewer.\n"
    )

    return Agent(
        name="Project Planning Agent",
        handoff_description="Creates day-level project schedules from estimate tasks.",
        instructions=instructions,
    )


def build_run_config(model_name: str | None = None) -> RunConfig:
    return RunConfig(model=model_name or "gpt-5-mini-2025-08-07")


def build_plan_messages(payload: Dict[str, Any]) -> list[dict[str, Any]]:
    """Embed the planning payload in a single user message."""

    text = (
        "Plan this renovation schedule using the payload below.\n"
        "Use the provided slots as sequential work days and prioritise safety, dependencies, and crew limits.\n"
        f"Payload JSON:\n{json.dumps(payload, ensure_ascii=False)}"
    )
    return [{"role": "user", "content": [{"type": "input_text", "text": text}]}]
