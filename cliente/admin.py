from django.contrib import admin
from .models import Cliente

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'tipo_cliente',)
    search_fields = ('nome', 'cnpj', 'tipo_cliente',) 
    