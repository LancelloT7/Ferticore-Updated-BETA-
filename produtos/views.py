from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto
from django.contrib import messages
from django.contrib.messages import constants

def cadProduto(request):
    if request.session.get('logado') == True: 
        if request.method == "GET":
            return render(request, 'cadProduto.html')
        elif request.method == "POST":
            nome = request.POST.get('nome')
            quantidade = request.POST.get('quantidade')

            if not nome or not quantidade:  # Verifica se nome ou quantidade estão vazios
                messages.add_message(request, constants.ERROR, 'Nome e quantidade são obrigatórios.')
                return render(request, 'cadProduto.html')
            try:
                quantidade = int(quantidade)  # Converte a quantidade para inteiro
                produto = Produto(nome=nome, quantidade=quantidade)  # Cria o objeto Produto
                produto.save()  # Salva o produto no banco de dados
                messages.add_message(request, constants.SUCCESS, 'Produto cadastrado com sucesso')  # Mensagem de sucesso
                return render(request, 'cadProduto.html') # Retorna uma resposta
            except ValueError:
                messages.add_message(request, constants.ERROR, 'A quantidade deve ser um número inteiro.')
                return render(request, 'cadProduto.html')

            return render(request, 'cadProduto.html')
    else:
        messages.add_message(request, constants.ERROR, 'Faça login para acessar o sistema')
        return render(request, 'login.html')
    