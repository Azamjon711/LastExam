from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from clients.models import Client
from blog.models import BlogPost
from staff.models import Staff


class HomePageView(View):
    def get(self, request):
        products = Product.objects.all()
        clients = Client.objects.all()
        posts = BlogPost.objects.all()
        context = {
            "products": products,
            "clients": clients,
            "posts": posts,

        }
        return render(request, "main/index.html", context)



class ContactPageView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            return render(request, "main/contact.html")


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password_1"]
        confirm_password = request.POST["password_2"]

        if password == confirm_password:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            checkUser = User.objects.filter(username=username, password=password)
            if checkUser:
                return render(request, "auth/register.html")
            else:
                user = User(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password)
                user.save()
                return redirect('login')
        else:
            return render(request, "auth/register.html")


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            "form": form
        }
        return render(request, "auth/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        data = {
            "username": username,
            "password": password
        }

        loginForm = AuthenticationForm(data=data)

        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect("home")
        else:
            form = UserLoginForm()
            context = {
                "form": form
            }
            return render(request, "auth/login.html")


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")








