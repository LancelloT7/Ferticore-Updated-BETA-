from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url=('/autenticacao/auth'))
def inicio(request): 
    return render (request, 'inicio.html')
    
    
def sair(request):
    logout(request)
    return redirect('/autenticacao/auth')
    
        
        
      