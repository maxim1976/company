from django.db import models


class Service(models.Model):
    """Services offered on the landing page."""

    icon = models.CharField(max_length=50, help_text="Lucide icon name (e.g., 'Globe', 'Zap', 'Bot')")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class PortfolioProject(models.Model):
    """Portfolio projects showcase."""

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.URLField(max_length=500, help_text="Image URL")
    link = models.URLField(max_length=500, blank=True, help_text="Project demo link")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    """Contact form submissions."""

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, help_text="Email or Line ID")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"
