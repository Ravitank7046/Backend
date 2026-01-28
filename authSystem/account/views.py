from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import FormView
from django.contrib import messages
from account.forms import RegistrationForm
from account.models import User
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.urls import reverse
from account.utils import send_activation_email

class HomeView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'account/home.html')

class LoginView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'account/login.html')
    
    def post(self,request,*args, **kwargs):
        return render(request,'customer/dashboard.html')
    
class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'account/register.html' 
    def form_valid(self,form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_active = False
        user.save()
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = reverse('activate',kwargs={'uid64':uidb64,'token':token})
        activation_url = f'{settings.SITE_DOMAIN}{activation_link}'
        send_activation_email(user.email,activation_url)
        messages.success(self.request,"Registration Email Send Successfully")
        return redirect('login')

class CustomPasswordResetView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'account/password_reset.html')

class PassowordResetConfirmView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'account/password_reset_confirm.html')

class LogoutView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'account/logout.html')
