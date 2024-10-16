from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants

def inicio(request):
    if request.session.get('logado') == True:    
        return render (request, 'inicio.html')
    else:
        messages.add_message(request, constants.ERROR, 'Faça login para acessar o sistema')
        return render(request, 'login.html')
    
def sair(request):
    request.session.flush()  # Remove todos os dados da sessão, efetivamente desconectando o usuário
    return redirect('/autenticacao/auth')
        
        
      