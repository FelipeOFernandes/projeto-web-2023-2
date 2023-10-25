from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    dataDeUltimaCompra= models.DateField()
    quantidade = models.IntegerField()

class Prato(models.Model):
    produtos = models.ManyToManyField(Produto)
    preco: models.FloatField()


class PratoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
