from __future__ import annotations

from decimal import Decimal
from typing import List

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import Truncator

from .models import ContractorLead, EstimateResult


def _build_headline(result: EstimateResult) -> str:
    job = result.job
    parts: List[str] = []
    if job.project:
        if job.project.name:
            parts.append(job.project.name)
        if job.project.zip:
            parts.append(job.project.zip)
    if job.title:
        parts.append(job.title)
    if not parts:
        parts.append(f"Job #{job.id}")
    return " • ".join(parts)


def _build_summary(result: EstimateResult, payload: dict) -> str:
    job = result.job
    pieces: List[str] = []
    if job.instructions:
        pieces.append(job.instructions.strip())

    raw_summary = payload.get("metadata", {}).get("raw_summary")
    if isinstance(raw_summary, dict):
        reasoning = raw_summary.get("estimate_reasoning")
        if reasoning:
            pieces.append(str(reasoning).strip())
        actions = raw_summary.get("future_actions")
        if isinstance(actions, list) and actions:
            lines = ", ".join(str(a) for a in actions[:5])
            pieces.append(f"Next steps: {lines}")
    elif isinstance(raw_summary, str) and raw_summary:
        pieces.append(raw_summary.strip())

    summary = "\n\n".join(pieces)
    return Truncator(summary).chars(1200)


@receiver(post_save, sender=EstimateResult)
def create_contractor_lead_on_result(sender, instance: EstimateResult, created: bool, **kwargs):
    if not created:
        return

    job = instance.job
    if not job:
        return

    # Only post leads for contractor-oriented jobs by default
    if getattr(job, "agent_kind", "").lower() not in {"contractor", "home_project"}:
        return

    if hasattr(instance, "contractor_lead"):
        return

    payload = ContractorLead.build_payload_from_result(instance)
    total_cost: Decimal = payload.get("total_cost") or Decimal("0")

    headline = _build_headline(instance)
    summary = _build_summary(instance, payload)

    with transaction.atomic():
        ContractorLead.objects.create(
            result=instance,
            job=job,
            headline=headline,
            summary=summary,
            total_cost=total_cost,
            line_items=payload.get("items", []),
            appendix=payload.get("appendix", {}),
            metadata=payload.get("metadata", {}),
        )
