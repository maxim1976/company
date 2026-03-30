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


class PricingPlan(models.Model):
    """Pricing plans for services."""

    BILLING_CHOICES = [
        ('one_time', 'One-time'),
        ('monthly', 'Monthly'),
        ('both', 'Both'),
    ]

    name_zh = models.CharField(max_length=100, help_text="Plan name in Chinese")
    name_en = models.CharField(max_length=100, help_text="Plan name in English")
    description_zh = models.TextField(help_text="Plan description in Chinese")
    description_en = models.TextField(help_text="Plan description in English")
    price_one_time = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="One-time price in TWD")
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Monthly price in TWD")
    features = models.JSONField(default=list, help_text='List of features: [{"name_zh": "...", "name_en": "...", "included": true}]')
    billing_period = models.CharField(max_length=20, choices=BILLING_CHOICES, default='one_time')
    plan_type = models.CharField(max_length=20, default='basic', help_text="CSS class type: basic, standard, advanced")
    sub_note = models.CharField(max_length=200, blank=True, help_text="Small note below price, supports HTML")
    is_highlighted = models.BooleanField(default=False, help_text="Mark as recommended plan")
    cta_text_zh = models.CharField(max_length=50, default="立即開始", help_text="CTA button text in Chinese")
    cta_text_en = models.CharField(max_length=50, default="Get Started", help_text="CTA button text in English")
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name_zh} / {self.name_en}"


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
