from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url=('/autenticacao/auth'))
def cadProduto(request): 
    if request.method == "GET":
        return render(request, 'cadProduto.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        formula = request.POST.get('formula')
        preco = request.POST.get('preco')
<<<<<<< HEAD
        img = request.FILES.get('img')
=======
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955

        if not nome or not formula:  # Verifica se nome ou quantidade estão vazios
            messages.add_message(request, constants.ERROR, 'Nome e formula são obrigatórios.')
            return render(request, 'cadProduto.html')
        try:
            if Produto.objects.filter(nome=nome):
                messages.add_message(request, constants.ERROR, 'Produto já cadastrado')
            else:    
<<<<<<< HEAD
                produto = Produto(nome=nome, formula=formula, preco=preco, img=img)  # Cria o objeto Produto
=======
                produto = Produto(nome=nome, formula=formula, preco=preco)  # Cria o objeto Produto
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955
                produto.save()  # Salva o produto no banco de dados
                messages.add_message(request, constants.SUCCESS, 'Produto cadastrado com sucesso')  # Mensagem de sucesso
                return render(request, 'cadProduto.html') # Retorna uma resposta
        except ValueError:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar produto.')
            return render(request, 'cadProduto.html')

<<<<<<< HEAD
        return render(request, 'listar_produto.html')
    
@login_required(login_url='/autenticacao/auth')
def listar_produtos(request):
    pesquisa = request.GET.get('pesquisa', '') 
    if pesquisa:
        produtos = Produto.objects.filter(nome__icontains=pesquisa)  
    else:
        produtos = Produto.objects.all()  
    return render(request, 'listar_produto.html', {'produtos': produtos})
=======
        return render(request, 'cadProduto.html')
    
@login_required(login_url=('/autenticacao/auth'))    
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produto.html', {'produtos':produtos })
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955

    
    