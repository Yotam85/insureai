from django.test import TestCase

from .utils import image_to_b64, pdf_bytes_to_images
from weasyprint import HTML



@shared_task(bind=True, max_retries=3, autoretry_for=(Exception,))
def run_estimate(self, job_id):
    job = EstimateJob.objects.select_related().get(pk=job_id)
    images = []

    for up in job.uploads.all():
        if up.mime.startswith("image/"):
            images.append(image_to_b64(up.file))
        else:  # PDF or DWG exported to PDF beforehand
            images.extend([image_to_b64(p) for p in pdf_bytes_to_images(up.file.read())])

    # Vision prompt
    messages = [{
        "role": "user",
        "content": [
            {"type": "input_text",
             "text": f"Claim {job.claim_number}: "
                     f"{job.property_type} / {job.damage_type}. "
                     "Extract repair cost, confidence %, days and breakdown."},
            *[{"type": "input_image", "image_url": img} for img in images]
        ]
    }]
    schema = {...}  # JSON schema omitted for brevity

    resp = client.responses.create(
        model="gpt-4o-mini",
        input=messages,
        text={"format": {"type": "json_schema", "schema": schema, "strict": True}},
        temperature=0
    )  # OpenAI docs :contentReference[oaicite:11]{index=11}

    data = json.loads(resp.output_text)
    EstimateResult.objects.create(
        job=job,
        cost=Decimal(data["repair_cost"]),
        confidence=data["confidence"],
        days_min=data["days"][0],
        days_max=data["days"][1],
        summary=data["summary"],
        breakdown=data["breakdown"],
    )
    job.status = "DONE"
    job.save()








# If you previously had `schema = {...}`, now do:

