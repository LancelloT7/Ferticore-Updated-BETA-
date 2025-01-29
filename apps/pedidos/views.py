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
from django.db.models import Sum

@login_required(login_url='/autenticacao/auth')
def cadPedidos(request):      
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    funcionarios = Funcionario.objects.all()

    if request.method == "GET":
        return render(request, 'cad_pedidos.html', {
            'produtos': produtos,
            'clientes': clientes,
            'funcionarios': funcionarios
        })
        
    elif request.method == "POST":
        nome_cliente = request.POST.get('nome_cliente')
        produto_ids = request.POST.getlist('produto')  # Lista dos ids dos produtos
        quantidades = request.POST.getlist('quantidade')  # Lista de quantidades correspondentes
        
        funcionario_id = request.POST.get('funcionario')
        
        cliente = Cliente.objects.get(id=nome_cliente)
        funcionario = Funcionario.objects.get(id=funcionario_id)

        # Criação do pedido
        pedido = Pedido(nome_cliente=cliente, funcionario=funcionario)
        pedido.save()  

        # Alteração para garantir que os produtos sejam armazenados como um dicionário
        produtos_no_pedido = {}
        for produto_id, quantidade in zip(produto_ids, quantidades):
            produto = Produto.objects.get(id=produto_id)
            
            # Verificar se o produto já existe, somar as quantidades
            if produto_id in produtos_no_pedido:
                produtos_no_pedido[produto_id] += float(quantidade)  # Somar a quantidade
            else:
                produtos_no_pedido[produto_id] = float(quantidade)  # Adicionar novo produto

        # Salva os produtos no pedido
        pedido.produtos = produtos_no_pedido
        pedido.save()  

        messages.add_message(request, constants.SUCCESS, 'Pedido cadastrado com sucesso')
        return redirect('/pedidos/cadastrar_pedidos')




from decimal import Decimal

from decimal import Decimal

@login_required(login_url='/autenticacao/auth')
def listar_pedidos(request):
    # Obtém os parâmetros de filtro
    produto_id = request.GET.get('produto', None)
    cliente_id = request.GET.get('cliente', None)
    funcionario_id = request.GET.get('funcionario', None)

    pedidos = Pedido.objects.all()

    # Filtra por produto se o filtro estiver presente
    if produto_id:
        pedidos = pedidos.filter(produtos__has_key=produto_id)

    # Filtra por cliente se o filtro estiver presente
    if cliente_id:
        pedidos = pedidos.filter(nome_cliente_id=cliente_id)

    # Filtra por funcionário se o filtro estiver presente
    if funcionario_id:
        pedidos = pedidos.filter(funcionario_id=funcionario_id)

   


    # Obtém as listas de produtos, clientes e funcionários para o filtro
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    funcionarios = Funcionario.objects.all()

    return render(request, 'listar_pedidos.html', {
        'pedidos': pedidos,
        'produtos': produtos,
        'clientes': clientes,
        'funcionarios': funcionarios
    })






@login_required(login_url='/autenticacao/auth')
def finalizar_pedido(request, pedido_id):
    # Tenta buscar o pedido com o cod fornecido
    pedido = get_object_or_404(Pedido, cod=pedido_id)  # Altere 'id' para 'cod'
    
    # Verifique se o pedido já foi finalizado ou não
    if pedido.status != 'Concluído':  # Verificando se o pedido não está 'Concluído'
        # Atualiza o status para "Concluído"
        pedido.status = 'Concluído'
        pedido.save()
        
        messages.success(request, "Finalizado")
    else:
        messages.warning(request, "Este pedido já foi finalizado.")

    return redirect('listar_pedidos')  # Redireciona de volta para a lista de pedidos





def detalhes_pedido(request, pedido_id):
    # Tenta buscar o pedido com o ID fornecido
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    # Calculando o total do pedido (isso pode ser feito diretamente no modelo, se já tiver uma função)
    total_pedido = pedido.total_pedido()

    # Renderize o template com os dados do pedido
    return render(request, 'detalhes_pedido.html', {
        'pedido': pedido,
        'total_pedido': total_pedido
    })

