from django.db import models
from produtos.models import Produto
from funcionarios.models import Funcionario
from cliente.models import Cliente
from django.db import models
from django.db import models
from django.db.models import JSONField
from decimal import Decimal

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]

    data_pedido = models.DateTimeField(auto_now_add=True)  # Data do pedido
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)  # Relaciona o pedido ao funcionário
    cod = models.AutoField(primary_key=True)  # Código do pedido

    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relaciona o pedido ao cliente

    nome_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)  # Relaciona o pedido ao cliente

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')  # Status do pedido

    # Usando JSONField para armazenar produtos e quantidades
    produtos = models.JSONField(default=dict)  # Ex: {"produto_id": quantidade}



    def produtos_no_pedido(self):
        """
        Retorna uma lista de dicionários com informações detalhadas dos produtos no pedido.
        """
        produtos_detalhados = []
        for produto_id, quantidade in self.produtos.items():
            try:
                produto = Produto.objects.get(id=produto_id)
                produtos_detalhados.append({
                    'produto': produto,
                    'quantidade': quantidade,
                    'total': produto.preco * Decimal(quantidade),
                })
            except Produto.DoesNotExist:
                continue
        return produtos_detalhados
    


    def __str__(self):
        produtos_nomes = ", ".join(str(produto['nome']) for produto in self.produtos.values())  # Obtém os nomes dos produtos
        return (f"Pedido {self.cod} - "
                f"Cliente: {self.nome_cliente} - "
                f"Funcionário: {self.funcionario} - "
                f"Data do Pedido: {self.data_pedido.strftime('%d/%m/%Y %H:%M')} - "
                f"Status: {self.status} - "
                f"Produtos: {produtos_nomes}")
    
    def total_pedido(self):
        """
        Calcula o total do pedido, somando os totais de cada produto.
        """
        total = Decimal(0)  # Inicializa com Decimal
        for produto_id, quantidade in self.produtos.items():
            try:
                produto = Produto.objects.get(id=produto_id)
                total += produto.preco * Decimal(quantidade)  # Converte quantidade para Decimal
            except Produto.DoesNotExist:
                continue  # Se o produto não for encontrado, ignora
        return total

    def adicionar_quantidade(self, produto, quantidade):
        """
        Adiciona ou atualiza a quantidade de um produto no pedido.
        """
        self.produtos[str(produto.id)] = quantidade
        self.save()

    
    