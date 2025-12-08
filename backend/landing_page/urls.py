from django.urls import path

from . import views

app_name = 'landing_page'

urlpatterns = [
    # Template views
    path("", views.landing_page_view, name="home"),
    path("contact/", views.contact_form_view, name="contact"),
    
    # API endpoints (optional)
    path("api/services/", views.ServiceListView.as_view(), name="service-list"),
    path("api/portfolio/", views.PortfolioListView.as_view(), name="portfolio-list"),
    path("api/contact/", views.ContactCreateView.as_view(), name="contact-create"),
]
