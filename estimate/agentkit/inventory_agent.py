from __future__ import annotations

from typing import Dict, Any, Tuple
import json

from agents import Agent, RunConfig

STRICT_JSON = (
    "Return ONLY raw JSON that exactly matches the schema. "
    "Do NOT include any prose, explanations, or markdown fences."
)

INVENTORY_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "inventory": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "quantity": {"type": "number", "minimum": 0},
                    "unit": {"type": "string"},
                    "unit_cost": {"type": "number", "minimum": 0}
                },
                "required": ["name", "quantity", "unit", "unit_cost"],
                "additionalProperties": False
            }
        }
    },
    "required": ["inventory"],
    "additionalProperties": False
}


def build_inventory_agent(*, currency: str = "USD") -> Agent:
    """
    Build an agent that converts estimate line items and context into a bill-of-materials style
    inventory list suitable for the sidebar editor. Output must match INVENTORY_SCHEMA.
    """
    header = {
        "currency": currency,
        "note": "Inventory is a bill of materials; do not include labor-only items.",
    }
    instructions = (
        "You are a construction estimator specializing in material takeoffs.\n"
        "You brack each line item into detils, and aff all the matireals this taks needs. For example if a line itme is - to replace drywall - we need scroes, tape, joint compound, etc. \n"
        "Given claim or estimate line items, convert them into a concise inventory (bill of materials).\n"
        "Merge duplicates, use realistic units (EA/LF/SF), and reasonable unit_cost based on context.\n"
        "Exclude pure labor items; materials only.\n"
        f"{STRICT_JSON}\n\n"
        "Header (context, include when relevant):\n"
        f"{json.dumps(header, indent=2)}\n\n"
        "SCHEMA (copy exactly):\n"
        f"{json.dumps(INVENTORY_SCHEMA, indent=2)}\n\n"
        "Your output must be a single JSON object with an 'inventory' array."
    )

    return Agent(
        name="Inventory Agent",
        handoff_description="Generates a material inventory from estimate line items.",
        instructions=instructions,
    )


def build_run_config(model_name: str | None = None) -> RunConfig:
    return RunConfig(model=model_name or "gpt-5-2025-08-07")


def build_inventory_message(items_payload: Any, *, currency: str = "USD") -> list[dict[str, Any]]:
    """
    Build a single user message with the normalized estimate items embedded as JSON.
    """
    text = (
        "Create a materials inventory from these estimate items. "
        "Focus on materials only. Return only JSON.\n\n"
        f"Currency: {currency}\n"
        "Estimate items JSON follows:\n"
        f"{json.dumps(items_payload, ensure_ascii=False)}"
    )
    return [{"role": "user", "content": [{"type": "input_text", "text": text}]}]

