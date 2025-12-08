from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from rest_framework import generics, status
from rest_framework.response import Response

from .models import ContactSubmission, PortfolioProject, Service
from .serializers import (
    ContactSubmissionSerializer,
    PortfolioProjectSerializer,
    ServiceSerializer,
)


# Template-based views
def landing_page_view(request):
    """Main landing page with all sections."""
    context = {
        'services': Service.objects.filter(is_active=True),
        'portfolio': PortfolioProject.objects.filter(is_active=True),
    }
    return render(request, 'landing_page/index.html', context)


@require_http_methods(["POST"])
def contact_form_view(request):
    """Handle contact form submission."""
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    
    if name and email and message:
        ContactSubmission.objects.create(
            name=name,
            email=email,
            message=message
        )
        messages.success(request, '感謝您！訊息已成功送出。 Thank you! Your message has been sent successfully.')
    else:
        messages.error(request, '請填寫所有欄位。 Please fill in all fields.')
    
    return redirect('/#contact')


# API views (keep for potential future use)
class ServiceListView(generics.ListAPIView):
    """List all active services."""

    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class PortfolioListView(generics.ListAPIView):
    """List all active portfolio projects."""

    queryset = PortfolioProject.objects.filter(is_active=True)
    serializer_class = PortfolioProjectSerializer


class ContactCreateView(generics.CreateAPIView):
    """Submit a contact form."""

    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Thank you! Your message has been sent successfully."},
            status=status.HTTP_201_CREATED,
        )
