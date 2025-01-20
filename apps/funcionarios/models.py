from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nome}, {self.cargo}'