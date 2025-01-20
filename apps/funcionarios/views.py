from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from .models import Funcionario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url=('/autenticacao/auth'))

def cadastrar_funcionario(request):
    funcionarios = Funcionario.objects.all() 
    if request.method == "GET":
        return render(request, 'cadastro_funcionario.html', {'funcionarios': funcionarios})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        if Funcionario.objects.filter(nome=nome).exists():
            messages.add_message(request, constants.ERROR, 'Funcionário já cadastrado')
            return redirect('/funcionario/cadastrar')
        else:
            funcionario = Funcionario(nome = nome, cargo = cargo)
            funcionario.save()
            messages.add_message(request, constants.SUCCESS, 'Funcionario cadastrado com sucesso')
        return redirect('/funcionario/cadastrar')
    