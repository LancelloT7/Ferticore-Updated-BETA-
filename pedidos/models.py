from django.db import models
from produtos.models import Produto

class Pedido(models.Model):
    data_pedido = models.DateTimeField(auto_now_add=True)
    cod = models.AutoField(primary_key=True)
    produto = models.ManyToManyField(Produto)  # Relaciona o Produto com o Pedido
    nome_cliente = models.CharField(max_length=100)
    
    def __str__(self):
        produtos_nomes = ", ".join(str(produto) for produto in self.produto.all())  # Obtém os nomes dos produtos
        return f"Pedido {self.cod} - {self.nome_cliente} - Produtos: {produtos_nomes}"