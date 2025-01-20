from django.contrib import admin
from .models import Pedido, Produto

# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('data_pedido', 'cod', 'nome_cliente', )
=======
    list_display = ('data_pedido', 'cod', 'nome_cliente',)
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955

    
    
