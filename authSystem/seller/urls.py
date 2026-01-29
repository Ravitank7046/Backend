from django.urls import path
from seller.views import SellerDashboardView,SellerPasswordChangeView

urlpatterns = [
    path('dashboard/',SellerDashboardView.as_view(),name="seller_dashboard"),
    path('password_change/', SellerPasswordChangeView.as_view(), name="seller_password_change"),
]