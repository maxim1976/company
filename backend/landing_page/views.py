from rest_framework import generics, status
from rest_framework.response import Response

from .models import ContactSubmission, PortfolioProject, Service
from .serializers import (
    ContactSubmissionSerializer,
    PortfolioProjectSerializer,
    ServiceSerializer,
)


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
