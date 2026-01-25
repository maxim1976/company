from django.contrib import admin

from .models import ContactSubmission, PortfolioProject, PricingPlan, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "icon", "order", "is_active", "updated_at"]
    list_editable = ["order", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["title", "description"]


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "order", "is_active", "updated_at"]
    list_editable = ["order", "is_active"]
    list_filter = ["is_active", "category"]
    search_fields = ["title", "description"]


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ["name_display", "price_display", "billing_period", "is_highlighted", "order", "is_active", "updated_at"]
    list_editable = ["order", "is_active", "is_highlighted"]
    list_filter = ["is_active", "billing_period", "is_highlighted"]
    search_fields = ["name_zh", "name_en", "description_zh", "description_en"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = [
        ("Names", {
            "fields": ["name_zh", "name_en"]
        }),
        ("Pricing", {
            "fields": ["price_one_time", "price_monthly", "billing_period"]
        }),
        ("Description & Features", {
            "fields": ["description_zh", "description_en", "features"]
        }),
        ("Call-to-Action", {
            "fields": ["cta_text_zh", "cta_text_en"]
        }),
        ("Settings", {
            "fields": ["order", "is_active", "is_highlighted"]
        }),
        ("Metadata", {
            "fields": ["created_at", "updated_at"],
            "classes": ["collapse"]
        }),
    ]

    def name_display(self, obj):
        return f"{obj.name_zh} / {obj.name_en}"
    name_display.short_description = "Plan Name"

    def price_display(self, obj):
        prices = []
        if obj.price_one_time:
            prices.append(f"NT${obj.price_one_time:,.0f}")
        if obj.price_monthly:
            prices.append(f"NT${obj.price_monthly:,.0f}/mo")
        return " + ".join(prices) if prices else "No price"
    price_display.short_description = "Price"


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "is_read", "created_at"]
    list_editable = ["is_read"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["name", "email", "message"]
    readonly_fields = ["name", "email", "message", "created_at"]
