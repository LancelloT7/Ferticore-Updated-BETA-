from django.db import models
from produtos.models import Produto
from funcionarios.models import Funcionario
from cliente.models import Cliente

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]

    data_pedido = models.DateTimeField(auto_now_add=True)  # Data do pedido
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
  # Relaciona o pedido ao funcionário
    cod = models.AutoField(primary_key=True)  # Código do pedido
    produto = models.ManyToManyField(Produto)  # Relaciona o Produto com o Pedido
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)  # Relaciona o pedido ao cliente
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')  # Status do pedido

    def __str__(self):
        produtos_nomes = ", ".join(str(produto) for produto in self.produto.all())  # Obtém os nomes dos produtos
        return (f"Pedido {self.cod} - "
                f"Cliente: {self.nome_cliente} - "
                f"Funcionário: {self.funcionario} - "
                f"Data do Pedido: {self.data_pedido.strftime('%d/%m/%Y %H:%M')} - "
                f"Status: {self.status} - "
                f"Produtos: {produtos_nomes}")
    
    