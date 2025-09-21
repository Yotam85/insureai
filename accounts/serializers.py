from __future__ import annotations

from rest_framework import serializers
from .models import ContractorProfile, ContractorTag


class ContractorTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorTag
        fields = ["id", "name"]


class ContractorProfileSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=ContractorTag.objects.all(), many=True, required=False)
    email = serializers.EmailField(source="user.email", read_only=True)
    role = serializers.CharField(source="user.role", read_only=True)
    trades = serializers.ListField(child=serializers.CharField(max_length=80), required=False)
    project_sizes = serializers.ListField(child=serializers.CharField(max_length=80), required=False)
    project_types = serializers.ListField(child=serializers.CharField(max_length=80), required=False)
    years_experience = serializers.ChoiceField(choices=ContractorProfile.YEARS_EXPERIENCE_CHOICES, allow_blank=True, required=False)
    attachment = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = ContractorProfile
        fields = [
            "email", "role",
            "full_name", "company",
            "phone", "website", "license_number",
            "trades", "zip_codes", "years_experience",
            "insured", "bonded",
            "project_sizes", "project_types",
            "availability", "how_heard", "notes",
            "attachment",
            "photo", "tags",
            "address_line1", "address_line2", "city", "state", "postal_code", "country",
            "bio",
            "identity_status",
        ]
        read_only_fields = ("identity_status",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Ensure list fields always present as lists for the frontend form
        for key in ("trades", "project_sizes", "project_types"):
            if data.get(key) is None:
                data[key] = []
        return data


class ContractorIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorProfile
        fields = ["identity_number", "identity_document"]
