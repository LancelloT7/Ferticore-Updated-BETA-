from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from django.contrib import messages

def cadProduto(request):
    if request.method == "GET":
        return render(request, 'cadProduto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')

        if not nome or not quantidade:  # Verifica se nome ou quantidade estão vazios
            messages.error(request, "Nome e quantidade são obrigatórios.")
            return render(request, 'cadProduto.html')

        try:
            quantidade = int(quantidade)  # Converte a quantidade para inteiro
            produto = Produto(nome=nome, quantidade=quantidade)  # Cria o objeto Produto
            produto.save()  # Salva o produto no banco de dados
            print('cadastrado')
            messages.success(request, "Produto cadastrado com sucesso!")  # Mensagem de sucesso
            return HttpResponse('Produto cadastrado')  # Retorna uma resposta
        except ValueError:
            messages.error(request, "A quantidade deve ser um número inteiro.")
            return render(request, 'cadProduto.html')

        return render(request, 'cadProduto.html')
