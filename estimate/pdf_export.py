# estimate/pdf_export.py
from __future__ import annotations

import io, json
from typing import Any, Dict, List, Union, Optional

from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

try:
    import jsonschema
except Exception:
    jsonschema = None  # optional

def _parse_result_final_output(final_output: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
    return json.loads(final_output) if isinstance(final_output, str) else final_output

def _fmt_money(amount, cur="USD"):
    try:
        return f"{cur} {float(amount):,.2f}"
    except Exception:
        return f"{cur} {amount}"

def _flatten_items(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Support both 'items' and legacy 'sections[].items'."""
    if isinstance(payload.get("items"), list):
        return payload["items"]

    items: List[Dict[str, Any]] = []
    for sec in payload.get("sections", []) or []:
        for it in (sec.get("items") or []):
            items.append(it)
    return items

def export_estimate_pdf_bytes(
    payload: Dict[str, Any],
    schema: Optional[Dict[str, Any]] = None,
    validate_schema: bool = False
) -> bytes:
    """Render estimate JSON -> PDF bytes."""

    # Optional: validate
    if validate_schema and schema and jsonschema:
        jsonschema.validate(instance=payload, schema=schema)

    version      = payload.get("version", "")
    generated_at = payload.get("generated_at", "")
    currency     = payload.get("currency", "USD")

    summary = payload.get("summary") or {}
    if "total_project_cost" not in summary:
        items = _flatten_items(payload)
        summary["total_project_cost"] = sum(float(i.get("TOTAL_PRICE", 0) or 0) for i in items)
    summary.setdefault("estimate_reasoning", "")
    summary.setdefault("future_actions", [])

    buf = io.BytesIO()
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=9, leading=11))
    styles.add(ParagraphStyle(name="Tiny",  parent=styles["BodyText"], fontSize=8, leading=10))

    doc = SimpleDocTemplate(
        buf, pagesize=LETTER, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )
    story = []

    # Title
    story.append(Paragraph("Insurance Damage Estimate", styles["Title"]))
    story.append(Spacer(1, 6))

    # Meta line
    meta_bits = []
    if version:      meta_bits.append(f"<b>Version:</b> {version}")
    if generated_at: meta_bits.append(f"<b>Generated:</b> {generated_at}")
    if currency:     meta_bits.append(f"<b>Currency:</b> {currency}")
    if meta_bits:
        story.append(Paragraph(" &nbsp;&nbsp; ".join(meta_bits), styles["Small"]))
        story.append(Spacer(1, 8))

    # Summary
    story.append(Paragraph(f"<b>Total Project Cost:</b> {_fmt_money(summary['total_project_cost'], currency)}", styles["BodyText"]))
    if summary.get("estimate_reasoning"):
        story.append(Spacer(1, 6))
        story.append(Paragraph("<b>Estimate reasoning</b>", styles["Heading4"]))
        story.append(Paragraph(summary["estimate_reasoning"], styles["Small"]))
 
    story.append(Spacer(1, 14))

    # Items table (if any)
    items = _flatten_items(payload)
    if items:
        def _p(x): return Paragraph(str(x), styles["Small"])
        table_header = ["ID", "Item", "Qty", "Unit", "Unit Price", "Tax", "Total", "Category"]
        rows = [table_header]
        for it in items:
            rows.append([
                _p(it.get("id", "")),
                _p(it.get("line_items") or it.get("description", "")),
                _p(it.get("QUANTITY", "")),
                _p(_fmt_money(it.get("UNIT_PRICE", 0), currency)),
                _p(_fmt_money(it.get("TAX", 0), currency)),
                _p(_fmt_money(it.get("TOTAL_PRICE", 0), currency)),
                _p(it.get("category", "")),
            ])

        avail = doc.width
        weights = [0.06, 0.36, 0.06, 0.07, 0.14, 0.08, 0.12, 0.10]
        col_widths = [avail * w for w in weights]

        tbl = Table(rows, colWidths=col_widths, repeatRows=1)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.grey),
            ("TEXTCOLOR",  (0,0), (-1,0), colors.whitesmoke),
            ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE",   (0,0), (-1,0), 10),
            ("ALIGN",      (2,1), (2,-1), "RIGHT"),
            ("ALIGN",      (4,1), (6,-1), "RIGHT"),
            ("GRID",       (0,0), (-1,-1), 0.5, colors.black),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.whitesmoke, colors.lightgrey]),
        ]))
        story.append(tbl)
    else:
        # Wind/Fire minimal payloads → show a small key/value table
        kv = []
        for k, v in payload.items():
            kv.append([Paragraph(f"<b>{k}</b>", styles["Small"]), Paragraph(str(v), styles["Small"])])
        if kv:
            tbl = Table(kv, colWidths=[140, 380])
            tbl.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black)]))
            story.append(tbl)

    # Appendix with Details/tags/source
    if items and any(i.get("Details") or i.get("tags") or i.get("source") for i in items):
        story.append(PageBreak())
        story.append(Paragraph("Appendix: Item Details", styles["Heading2"]))
        story.append(Spacer(1, 6))
        for it in items:
            story.append(Paragraph(f"<b>{it.get('id','')} — {it.get('line_items') or it.get('description','')}</b>", styles["BodyText"]))
            if it.get("Details"):
                story.append(Paragraph(it["Details"], styles["Small"]))
            tags = it.get("tags") or []
            src  = it.get("source") or {}
            extras = []
            if tags:
                extras.append("Tags: " + ", ".join(map(str, tags)))
            if src:
                parts = []
                if src.get("file"): parts.append(f"file: {src['file']}")
                if src.get("page"): parts.append(f"page: {src['page']}")
                if parts: extras.append("Source: " + ", ".join(parts))
            if extras:
                story.append(Paragraph(" &nbsp; | &nbsp; ".join(extras), styles["Tiny"]))
            story.append(Spacer(1, 8))

    doc.build(story)
    return buf.getvalue()
