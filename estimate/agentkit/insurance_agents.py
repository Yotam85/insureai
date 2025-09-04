# estimate/agentkit/insurance_agents.py
from __future__ import annotations

from typing import Optional, Tuple, Dict, Any, Sequence
from pathlib import Path
from functools import lru_cache
from copy import deepcopy
import json
import os
import logging

from agents import Agent, RunConfig
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────
# Unified knowledge base loader (cached)
# ─────────────────────────────────────────────────────────
@lru_cache(maxsize=1)
def unified_kb_text() -> str:
    env_path = os.environ.get("UNIFIED_KB_PATH")
    if env_path:
        p = Path(env_path)
        try:
            if p.exists():
                return p.read_text(encoding="utf-8")
        except Exception:
            log.exception("Failed reading UNIFIED_KB_PATH=%s", env_path)

    here = Path(__file__).parent
    p = here / "kb_unified.md"
    try:
        if p.exists():
            return p.read_text(encoding="utf-8")
    except Exception:
        log.exception("Failed reading %s", p)

    log.warning("Unified KB file not found. Proceeding with empty knowledge base.")
    return ""


STRICT_JSON = (
    "Return ONLY raw JSON that exactly matches the schema. "
    "Do NOT include any prose, explanations, or markdown fences."
)

# ─────────────────────────────────────────────────────────
# Base schema (canonical keys)
# ─────────────────────────────────────────────────────────
BASE_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "version":      {"type": "string"},
        "generated_at": {"type": "string", "format": "date-time"},
        "currency":     {"type": "string", "pattern": "^[A-Z]{3}$"},
        "workflow":     {"type": "string", "enum": ["home_project", "adjuster", "contractor"]},
        "location":     {"type": "string"},
        "items": {
            "type": "array",
            "minItems": 0,
            "items": {"$ref": "#/definitions/LineItem"}
        },
        "summary": {
            "type": "object",
            "properties": {
                "total_project_cost": {"type": "number"},
                "estimate_reasoning": {"type": "string"},
                "future_actions": {"type": "array", "items": {"type": "string"}}
            },
            "required": ["total_project_cost", "estimate_reasoning", "future_actions"],
            "additionalProperties": False
        }
    },
    "required": ["items", "summary"],
    "additionalProperties": False,
    "definitions": {
        "UnitCode": {
            "type": "string",
            "enum": [
                "EA","LF","SF","SQ","SY","HR","FT","YD","GL","GAL","CF","CY","BX",
                "KT","LB","TN","RL","RM","LN","MO","WK","DAY","PH","SET","ROLL","SHT",
                "PC","PR"
            ]
        },
        "LineItem": {
            "type": "object",
            "description": "Use canonical keys. TOTAL_PRICE = QUANTITY*UNIT_PRICE + TAX.",
            "properties": {
                "id":           {"type": ["integer","string"]},
                "line_items":   {"type": "string", "minLength": 1},
                "QUANTITY":     {"type": "number", "minimum": 0},
                "UNIT_PRICE":   {"type": "number", "minimum": 0},
                "TAX":          {"type": "number", "minimum": 0, "default": 0},
                "TOTAL_PRICE":  {"type": "number", "minimum": 0},
                "Details":      {"type": "string", "default": ""},
                "unit_code":    {"$ref": "#/definitions/UnitCode"},
                "category":     {"type": "string"},
                "tags":         {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
                "source": {
                    "type": "object",
                    "properties": {
                        "catalog_row": {"type": "string"},
                        "file": {"type": "string"},
                        "page": {"type": "integer", "minimum": 1}
                    },
                    "additionalProperties": False
                },
                "metadata": {"type": "object", "additionalProperties": True}
            },
            "required": ["id","line_items","QUANTITY","UNIT_PRICE","TOTAL_PRICE","unit_code","category"],
            "additionalProperties": False
        }
    }
}

def role_schema(role: str) -> Dict[str, Any]:
    """
    Per-request schema with 'workflow' pinned to a constant for the chosen role.
    You can also add/override per-role fields here.
    """
    s = deepcopy(BASE_SCHEMA)
    # Pin workflow to this role
    s["properties"]["workflow"] = {"const": role}
    # Example role-specific tweaks (uncomment/adjust as needed):
    # if role == "adjuster":
    #     s["properties"]["peril"] = {"type": "string", "enum": ["water","fire","wind","roof"]}
    #     s["required"] = list(set(s["required"] + ["peril"]))
    # if role == "contractor":
    #     s["properties"]["schedule_days"] = {"type": "number", "minimum": 0}
    # if role == "home_project":
    #     s["properties"]["goal"] = {"type": "string", "enum": ["renovation","flip","addition","repair"]}
    return s


# ─────────────────────────────────────────────────────────
# Prompt builders
# ─────────────────────────────────────────────────────────
def make_role_instructions(
    role: str,
    kb: str,
    schema: Dict[str, Any],
    settings: Dict[str, Any] | None = None,
) -> str:
    """
    Build the instructions for a role and EMBED the JSON schema text.
    Also inject runtime "header" fields the model must populate.
    """
    settings = settings or {}
    currency      = (settings.get("currency") or "USD").upper()
    location      = settings.get("location") or ""
    peril         = settings.get("peril") or ""
    property_type = settings.get("property_type") or ""  # "res" / "com" (or human readable)

    header_template = {
        "version": "1.0",
        "generated_at": "<ISO8601 timestamp>",
        "currency": currency,
        "workflow": role,               # MUST equal the role constant
        "location": location,           # optional
        # Optional context hints that the model should include when known:
        "peril": peril,                 # e.g., "water", "fire", "wind"
        "property_type": property_type  # e.g., "res", "com"
    }

    return (
        f"You are the {role.replace('_',' ').title()}.\n"
        "You will receive the user's description and images in the conversation input.\n"
        "Use the shared knowledge base for pricing vernacular and structure.\n"
        f"{STRICT_JSON}\n\n"
        "Before you start, populate these header fields exactly (use values shown or leave as empty strings if unknown):\n"
        f"{json.dumps(header_template, indent=2)}\n\n"
        "KNOWLEDGE BASE:\n"
        f"{kb}\n\n"
        "SCHEMA (copy exactly):\n"
        f"{json.dumps(schema, indent=2)}"
    )


def build_input_messages(user_text: str, data_uris: Sequence[str]) -> list[dict[str, Any]]:
    content: list[dict[str, Any]] = [{"type": "input_text", "text": user_text}]
    for uri in data_uris:
        content.append({"type": "input_image", "image_url": uri})
    return [{"role": "user", "content": content}]


# ─────────────────────────────────────────────────────────
# Build agents (settings are injected per request)
# ─────────────────────────────────────────────────────────
def build_insurance_agents(*, kb: str | None = None, settings: Dict[str, Any] | None = None) -> Tuple[Agent, Agent, Agent, Agent]:
    kb_text = kb if kb is not None else unified_kb_text()
    settings = settings or {}

    home_schema = role_schema("home_project")
    adj_schema  = role_schema("adjuster")
    con_schema  = role_schema("contractor")

    home_project_agent = Agent(
        name="Home Project Agent",
        handoff_description="Specialist for homeowner project planning. Outputs ONLY raw JSON conforming to the embedded schema.",
        instructions=make_role_instructions("home_project", kb_text, home_schema, settings),
    )
    adjuster_agent = Agent(
        name="Insurance Adjuster Agent",
        handoff_description="Specialist for insurance estimates and claim line items. Specialist for insurance estimates and claim line items. You provide fer and reliable estimates. Few expert guidlines: 1. if a block (roof slop, floor, wall etc.) is damage more then 40% you replace the entire block. 2. in case there are more then 3 contractors involved in the project yo add 10% to the claim pricing."
        "Outputs ONLY raw JSON conforming to the embedded schema.",
        instructions=make_role_instructions("adjuster", kb_text, adj_schema, settings),
    )
    contractor_agent = Agent(
        name="Contractor Agent",
        handoff_description="Specialist for contractor scope, bid line items, and schedule. Outputs ONLY raw JSON conforming to the embedded schema.",
        instructions=make_role_instructions("contractor", kb_text, con_schema, settings),
    )

    triage_agent = Agent(
        name="Role Triage Agent",
        instructions=(
            "Analyze the user's images and description like a senior PM/adjuster/contractor/architect. "
            "Choose the single best specialist: Home Project / Insurance Adjuster / Contractor. "
            "HAND OFF to that agent. The specialist must return ONLY raw JSON conforming to its schema. "
            "When handing off, preserve the original user message verbatim; do not summarize it.\n"
            f"{RECOMMENDED_PROMPT_PREFIX}"
        ),
        handoffs=[home_project_agent, adjuster_agent, contractor_agent],
    )

    return triage_agent, home_project_agent, adjuster_agent, contractor_agent


def build_agent(kind: Optional[str], *, kb: str | None = None, settings: Dict[str, Any] | None = None) -> Agent:
    triage, home, adjuster, contractor = build_insurance_agents(kb=kb, settings=settings)
    if not kind:
        return triage
    k = kind.lower()
    if k in {"home_project", "project", "renovation", "flip"}:
        return home
    if k in {"insurance", "adjuster", "claim", "estimate"}:
        return adjuster
    if k in {"contractor", "scope", "bid"}:
        return contractor
    return triage


def build_run_config(model_name: Optional[str] = None) -> RunConfig:
    return RunConfig(model=model_name or "gpt-5-mini-2025-08-07")
