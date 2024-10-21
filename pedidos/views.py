from django.shortcuts import render, redirect
from .models import Pedido
from produtos.models import Produto
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from funcionarios.models import Funcionario
from cliente.models import Cliente
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/autenticacao/auth')
def cadPedidos(request):      
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()  # Busque todos os produtos
    funcionarios = Funcionario.objects.all()

    if request.method == "GET":
        # Enviar todos os contextos em um único dicionário
        return render(request, 'cad_pedidos.html', {
            'produtos': produtos,
            'clientes': clientes,
            'funcionarios': funcionarios
        })
        
    elif request.method == "POST":
        nome_cliente = request.POST.get('nome_cliente')
        produto_ids = request.POST.getlist('produto')  # Recebe uma lista de IDs de produtos
        funcionario_id = request.POST.get('funcionario')  # Captura o ID do funcionário
        
        # Criar o pedido e associar o cliente
        cliente = Cliente.objects.get(id=nome_cliente)
        funcionario = Funcionario.objects.get(id=funcionario_id)

        # Criação do pedido
        pedido = Pedido(nome_cliente=cliente, funcionario=funcionario)
        pedido.save()

        # Associe cada produto ao pedido
        for produto_id in produto_ids:
            produto = Produto.objects.get(id=produto_id)  # Recupera o produto pelo ID
            pedido.produto.add(produto)  # Adiciona o produto ao pedido
        messages.add_message(request, constants.SUCCESS, 'Pedido cadastrado com sucesso')
        pedido.save()  # Salva o pedido com os produtos relacionados

        # Exibir mensagem de sucesso
        messages.add_message(request, constants.SUCCESS, 'Pedido cadastrado com sucesso')  
        return redirect('/pedidos/cadastrar_pedidos')  # Redireciona para a página inicial (ajuste a URL conforme necessário)

@login_required(login_url='/autenticacao/auth')
def listar_pedidos(request):
    pedidos = Pedido.objects.all()  # Busca todos os pedidos
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})  # Passa os pedidos para o template

@login_required(login_url='/autenticacao/auth')
def finalizar_pedido(request, pedido_id):
    # Obtém o pedido com base no código
    pedido = get_object_or_404(Pedido, cod=pedido_id)
    
    # Atualiza o status do pedido para 'Concluído'
    pedido.status = 'Concluído'
    pedido.save()
    
    # Redireciona para a lista de pedidos
    return redirect('listar_pedidos')
