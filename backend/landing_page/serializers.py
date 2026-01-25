from rest_framework import serializers

from .models import ContactSubmission, PortfolioProject, PricingPlan, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "icon", "title", "description"]


class PortfolioProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioProject
        fields = ["id", "title", "category", "description", "image", "link"]


class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = [
            "id", "name_zh", "name_en", "description_zh", "description_en",
            "price_one_time", "price_monthly", "features", "billing_period",
            "is_highlighted", "cta_text_zh", "cta_text_en"
        ]


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ["id", "name", "email", "message"]
        read_only_fields = ["id"]
