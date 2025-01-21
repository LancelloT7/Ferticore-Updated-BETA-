from django.contrib import admin
from .models import Pedido, Produto

# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):

    list_display = ('data_pedido', 'cod', 'nome_cliente', )
    list_display = ('data_pedido', 'cod', 'nome_cliente',)


    
    
