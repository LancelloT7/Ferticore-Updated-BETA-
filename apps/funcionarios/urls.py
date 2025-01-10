from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_funcionario, name = 'cadastrar_funcionario')
]