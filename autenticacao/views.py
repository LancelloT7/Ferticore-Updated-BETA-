from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json  # Certifique-se de importar json corretamente
from django.contrib.auth.models import User
from menu_principal.views import inicio
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "POST":
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        

        if User.objects.filter(username=login):
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado')
            return render (request, 'cadastro.html')
        
        # Cria e salva um novo usuário com a senha criptografada
        else:
            User.objects.create_user(username=login, password=senha)
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return render (request, 'login.html')
        
    elif request.method == "GET":
        return render (request, 'cadastro.html')
    

def auth(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        
        login_username = request.POST.get('login')
        senha = request.POST.get('senha')
        
        # Verifica se o usuário está autenticado
        usuario = authenticate(request, username=login_username, password=senha)
        
        if  not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos.')
            return redirect('/autenticacao/auth')
            
        else:
            login(request, usuario)  
            return redirect('/menu/opcoes')  # Redireciona para a página inicial
            


