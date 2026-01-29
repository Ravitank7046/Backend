from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import FormView
from django.contrib import messages
from account.forms import RegistrationForm
from account.models import User
from django.contrib.auth import authenticate, login

class HomeView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'account/home.html')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        # Redirect authenticated users to their dashboard
        if request.user.is_authenticated:
            if request.user.is_seller:
                return redirect('seller_dashboard')
            elif request.user.is_customer:
                return redirect('customer_dashboard')
        return render(request, 'account/login.html')
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            messages.error(request, "Both fields are required.")
            return redirect('login')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_seller:
                return redirect('seller_dashboard')
            elif user.is_customer:
                return redirect('customer_dashboard')
            else:
                messages.error(request, "You do not have permission to access this area")
                return redirect('home')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')    
class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'account/register.html' 
    
    def get(self, request, *args, **kwargs):
        # Redirect authenticated users to their dashboard
        if request.user.is_authenticated:
            if request.user.is_seller:
                return redirect('seller_dashboard')
            elif request.user.is_customer:
                return redirect('customer_dashboard')
        return super().get(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_active = True  # Activate user immediately - no email verification needed
        
        # Set user type based on selection
        user_type = self.request.POST.get('user_type', 'customer')
        if user_type == 'seller':
            user.is_seller = True
            user.is_customer = False
        else:
            user.is_customer = True
            user.is_seller = False
        
        user.save()
        messages.success(self.request, "Registration successful! You can now login.")
        return redirect('login')

class LogoutView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'account/logout.html')
