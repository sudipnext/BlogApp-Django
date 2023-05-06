from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from django.contrib import auth
# Create your views here.
#Login View
class LoginView(View):
    def get(self, request):
        return render(request, "authentication/login.html")
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return render(request, 'myblog/index.html')
#Logout View    
class RegisterView(View):
    def get(self, request):
        return render(request, "authentication/register.html")
    def post(self, request):
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username, password=password)
                user.set_password(password)
                user.save()
                return render(request, "authentication/login.html")
        else:
            return render(request, "authentication/register.html")

            
        return render(request, "authentication/register.html")
#Logout View
class LogOutView(View):
    def post(self, request):
        auth.logout(request)
        return redirect("login")
    
#UserValidation
