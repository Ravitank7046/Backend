# customer/urls.py
from django.urls import path
from customer.views import CustomerDashboardView, CustomerPasswordChangeView


urlpatterns = [
    path('dashboard/', CustomerDashboardView.as_view(), name="customer_dashboard"),
    path('password_change/', CustomerPasswordChangeView.as_view(), name="customer_password_change"),
]
