from django.contrib import admin

from .models import ContactSubmission, PortfolioProject, Service


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


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "is_read", "created_at"]
    list_editable = ["is_read"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["name", "email", "message"]
    readonly_fields = ["name", "email", "message", "created_at"]
