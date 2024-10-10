from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()  # Usando PositiveIntegerField sem max_length
    
    def __str__(self):
        return self.nome
