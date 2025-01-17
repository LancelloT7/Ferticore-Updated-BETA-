from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    formula = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    img = models.ImageField(upload_to='produtos/')

    
    def __str__(self):
        return f'{self.nome}, {self.formula}, {self.preco}, {self.disponivel}'
