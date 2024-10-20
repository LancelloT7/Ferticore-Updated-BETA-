from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from cliente.models import Cliente

# Create your views here.

def cadastrar_cliente(request):
    if request.session.get('logado') == True:
        if request.method == "GET":
            return render(request, 'cadastrar_cliente.html')
        elif request.method == "POST":
            nome = request.POST.get('nome')
            cnpj = request.POST.get('cnpj')
            tipo_cliente = request.POST.get('tipo_cliente')
            if Cliente.objects.filter(cnpj = cnpj).exists():
                messages.add_message(request, constants.ERROR, 'CNPJ já cadastrado')
                return redirect('/cliente/cadastrar_cliente')
            else:
                messages.add_message(request, constants.SUCCESS, 'Cliente cadastrado com sucesso')
                cliente = Cliente(nome = nome, cnpj = cnpj, tipo_cliente = tipo_cliente)
                cliente.save()
                return redirect('/cliente/cadastrar_cliente')
    else:
        messages.add_message(request, constants.ERROR, 'Faça login para acessar o sistema')
        return redirect('/autenticacao/auth')
