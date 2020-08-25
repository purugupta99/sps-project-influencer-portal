from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='home'),
    path('logout/', views.my_logout, name='logout')
]