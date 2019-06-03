# djangotemplates/signup/views.py
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from .models import User
# Add the two views we have been talking about  all this time :)
class SingnupPageView(TemplateView):
    template_name = "auth/singnup.html"

def RegisterView(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    repassword = request.POST.get("password_confirmation")

    User(emails=email, password=password, repeatpassword=repassword).save()

class LoginPageView(TemplateView):
    template_name = "auth/login.html"
    model = User


