from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('opcoes/', views.inicio, name='opcoes'),
    path('sair/', views.sair, name='sair'),
]