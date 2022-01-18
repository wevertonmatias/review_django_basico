from django.db import models

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=120, blank=False, null=False)
    endereco = models.CharField(max_length=255, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
