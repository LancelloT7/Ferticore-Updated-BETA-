from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido
from cliente.models import Cliente
from produtos.models import Produto


    

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
    
def sair(request):
    logout(request)
    return redirect('/autenticacao/auth')
    
        
        
      