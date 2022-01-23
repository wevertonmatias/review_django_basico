from django.db import models

# Create your models here.

class Dependente(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class CPF(models.Model):
    cpf = models.CharField(max_length=11)
    data_ext = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.cpf

class Cliente(models.Model):
    nome = models.CharField(max_length=120, blank=False, null=False)
    endereco = models.CharField(max_length=255, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE, null=True, blank=True)
    dependentes = models.ManyToManyField(Dependente, blank=True)
    foto = models.ImageField(upload_to="clientes_fotos")

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=120)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero


