
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.user_login, name='login'),
    path(r'restricted/', views.restricted, name='restricted'),
    path(r'logout/', views.user_logout, name='logout')
]
