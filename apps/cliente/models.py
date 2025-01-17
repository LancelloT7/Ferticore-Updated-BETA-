from django.db import models

# Create your models here.

class Cliente(models.Model):
    OP_CHOICES = [
        ('Revenda', 'Revenda'),
        ('Produtor', 'Produtor'),
        ('Usina', 'Usina'),
        ('Cooperativa', 'Cooperativa'),
        ('Granuladora', 'Granuladora'),
    ]

    nome = models.CharField(max_length=100)  # Nome do cliente
    cnpj = models.CharField(max_length=20)
    tipo_cliente = models.CharField(max_length=20, choices=OP_CHOICES)  # Tipo do cliente

    def __str__(self):
        return f'{self.nome}, {self.cnpj}, {self.tipo_cliente}'
                            