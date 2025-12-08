from django.urls import path

from . import views

urlpatterns = [
    path("services/", views.ServiceListView.as_view(), name="service-list"),
    path("portfolio/", views.PortfolioListView.as_view(), name="portfolio-list"),
    path("contact/", views.ContactCreateView.as_view(), name="contact-create"),
]
