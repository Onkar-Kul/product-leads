from django.urls import path

from leads.views import LeadCreateView, LeadsBetweenDatesAPIView, LeadProductCountView

urlpatterns = [
    path('create/', LeadCreateView.as_view(), name='lead-creation'),

    # Reporting APIs (Products Related)
    path('leads-between-dates/', LeadsBetweenDatesAPIView.as_view(), name='leads-between-dates'),
    path('products-count/', LeadProductCountView.as_view(), name='products-count'),
]
