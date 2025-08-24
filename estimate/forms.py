# estimate/forms.py
from django import forms
from .models import EstimateJob

class CaseInfoForm(forms.ModelForm):
    class Meta:
        model = EstimateJob
        fields = [
            "claim_number",
            "property_type",
            "damage_type",
        ]
        widgets = {
            "claim_number": forms.TextInput(attrs={
                "class": "w-full p-2 border rounded",
                "placeholder": "Claim # (e.g. CLM-2025-001234)",
            }),
            "property_type": forms.Select(attrs={
                "class": "w-full p-2 border rounded",
            }),
            "damage_type": forms.Select(attrs={
                "class": "w-full p-2 border rounded",
            }),
        }
