from django.contrib import admin
from .models import Produto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    pass

    list_display = ('nome', 'disponivel')
    search_fields = ('nome',)

    