from django.urls import path
from .views import HomePageView, UserRegisterView, UserLoginView, UserLogOutView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('auth/register', UserRegisterView.as_view(), name='register'),
    path('auth/login', UserLoginView.as_view(), name='login'),
    path('auth/logout', UserLogOutView.as_view(), name='logout'),
    path('contact/', ContactPageView.as_view(), name='contact'),


]
