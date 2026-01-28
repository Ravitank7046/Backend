from django.urls import path
from account.views import HomeView,LoginView,RegistrationView,CustomPasswordResetView,PassowordResetConfirmView,LogoutView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',RegistrationView.as_view(),name="register"),
    path('password_reset/',CustomPasswordResetView.as_view(),name="password_reset"),
    path('password_reset_confirm/<uid64>/<token>/',PassowordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('logout/',LogoutView.as_view(),name="logout")
]