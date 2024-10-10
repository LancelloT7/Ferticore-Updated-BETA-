from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pedido
from produtos.models import Produto



def cadPedidos(request):
    produtos = Produto.objects.all()  # Busque todos os produtos
    if request.method == "GET":
        return render(request, 'cad_pedidos.html', {'produtos': produtos})
    
    elif request.method == "POST":
        nome_cliente = request.POST.get('nome_cliente')
        produto_ids = request.POST.getlist('produto')  # Recebe uma lista de IDs de produtos

        # Crie o pedido sem associar os produtos ainda
        pedido = Pedido(nome_cliente=nome_cliente)
        pedido.save()

        # Associe cada produto ao pedido
        for produto_id in produto_ids:
            produto = Produto.objects.get(id=produto_id)  # Recupera o produto pelo ID
            pedido.produto.add(produto)  # Adiciona o produto ao pedido

        pedido.save()  # Salva o pedido com os produtos relacionados

        return HttpResponse('Pedido cadastrado com sucesso!')
    
    return redirect('inicio.html')

def listar_pedidos(request):
    pedidos = Pedido.objects.all()  # Busca todos os pedidos
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})  # Passa os pedidos para o template






# Create your views here.
