from django.contrib import admin
from .models import Produto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    pass
=======
    list_display = ('nome', 'disponivel')
    search_fields = ('nome',)
>>>>>>> ecf1ab31fdaa516378b83f9c0f99b20d30448955
    