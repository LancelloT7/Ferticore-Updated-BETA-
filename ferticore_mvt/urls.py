"""
URL configuration for ferticore_mvt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
    path('menu/', include('menu_principal.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('produtos/', include('produtos.urls')),
    path('', lambda request: render(request, 'login.html'), name='login'),
    path('funcionario/', include('funcionarios.urls')),
    path('cliente/', include('cliente.urls')),
]
<<<<<<< HEAD

if settings.DEBUG:  # Adicione apenas se estiver em modo DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955
