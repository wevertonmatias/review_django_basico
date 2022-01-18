from django.db import models

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=120, blank=False, null=False)
    endereco = models.CharField(max_length=255, blank=False, null=False)