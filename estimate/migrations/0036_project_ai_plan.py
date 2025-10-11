from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("estimate", "0035_estimateresult_total_cost"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="plan_ai_payload",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="project",
            name="plan_ai_response",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="project",
            name="plan_ai_updated",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

