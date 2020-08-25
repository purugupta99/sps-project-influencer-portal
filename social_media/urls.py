from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('', views.view_profile, name='profile'),
]