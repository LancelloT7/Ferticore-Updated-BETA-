from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('cadastrar_produto/', views.cadProduto, name ='cadProduto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos')
]
