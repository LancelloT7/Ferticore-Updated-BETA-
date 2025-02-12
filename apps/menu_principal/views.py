from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido
from cliente.models import Cliente
from produtos.models import Produto
from django.db.models import Sum


    

@login_required(login_url=('/autenticacao/auth'))
def inicio(request):
         
        return render(request, 'inicio.html')
    
@login_required(login_url=('/autenticacao/auth'))
def dashboard(request): 
    if request.method == "GET":
        # Conta o total de pedidos
        total_pedidos = Pedido.objects.count()
        total_clientes = Cliente.objects.count()
        total_produtos = Produto.objects.count()
       

        # Passa o total para o template
        context = {
            'total': total_pedidos,
            'cliente': total_clientes,
            'produto': total_produtos,
             
            # outros dados que você possa querer passar
        }

        

        return render(request, 'dashboard.html', context)
    



@login_required(login_url=('/autenticacao/auth'))
def dashboard2(request): 
    if request.method == "GET":
        # Calculando o total de pedidos por status
        pedidos_p = Pedido.objects.filter(status='Pendente').aggregate(total=Sum('total_pedido'))['total'] or 0
        pedidos_f = Pedido.objects.filter(status='Concluído').aggregate(total=Sum('total_pedido'))['total'] or 0
        pedidos_c = Pedido.objects.filter(status='Cancelado').aggregate(total=Sum('total_pedido'))['total'] or 0
        
        # Debug para verificar os valores
        print(f"Pedidos Pendentes: {pedidos_p}")
        print(f"Pedidos Concluídos: {pedidos_f}")
        print(f"Pedidos Cancelados: {pedidos_c}")

        # Passando os totais para o template
        context2 = {
            'Pendentes': pedidos_p,
            'Concluídos': pedidos_f,
            'Cancelados': pedidos_c, 
        }

        return render(request, 'inicio.html', context2)

    
    
def sair(request):
    logout(request)
    return redirect('/autenticacao/auth')
    
        
        
      