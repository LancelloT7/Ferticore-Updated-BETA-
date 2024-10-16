from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
import json  # Certifique-se de importar json corretamente
from django.contrib.auth.models import User
from menu_principal.views import inicio
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "POST":
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        
        # Cria e salva um novo usuário com a senha criptografada
        User.objects.create_user(username=login, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
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
            request.session['logado'] = True
            request.session['usuario_id'] = user.id
            request.session['nome_usuario'] = user.username
            return render(request, 'inicio.html')
        else:
            # Usuário não autenticado
            messages.add_message(request, constants.ERROR, 'Usuário ou senha invalidos')
            return redirect('/autenticacao/auth/')


