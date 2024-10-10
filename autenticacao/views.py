from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
import json  # Certifique-se de importar json corretamente
from django.contrib.auth.models import User
from menu_principal.views import inicio
from django.contrib.auth.hashers import make_password

def cadastro(request):
    if request.method == "POST":
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        
        # Cria e salva um novo usuário com a senha criptografada
        User.objects.create_user(username=login, password=senha)
        return render (request, 'login.html')
        
    elif request.method == "GET":
        return render (request, 'cadastro.html')
    

def auth(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        
        # Verifica se o usuário está autenticado
        user = authenticate(username=login, password=senha)
        
        if user is not None:
            # Usuário autenticado com sucesso
            return render(request, 'inicio.html')
        else:
            # Usuário não autenticado
            return HttpResponse("Usuário não cadastrado ou senha incorreta.")


