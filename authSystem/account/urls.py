from django.urls import path
from account.views import HomeView, LoginView, RegistrationView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegistrationView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name="logout")
]