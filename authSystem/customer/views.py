from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomerDashboardView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        # Ensure only customers can access
        if not request.user.is_customer:
            messages.error(request, "You do not have permission to access this page.")
            return redirect('home')
        return render(request, 'customer/dashboard.html')

class CustomerPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    login_url = '/login/'
    template_name = 'customer/password_change.html'
    success_url = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        # Ensure only customers can access
        if not request.user.is_customer:
            messages.error(request, "You do not have permission to access this page.")
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Password changed successfully")
        logout(self.request)
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error changing your password. Please try again later.")
        return super().form_invalid(form)
    
    def get(self,request,*args, **kwargs):
        return render(request,'customer/password_change.html')
