# customer/urls.py
from django.urls import path
from account.views import CustomerDashboardView, CustomerPasswordChangeView


urlpatterns = [
    path('', CustomerDashboardView.as_view(), name="dashboard"),
    path('password_change/', CustomerPasswordChangeView.as_view(), name="password_change"),
]
