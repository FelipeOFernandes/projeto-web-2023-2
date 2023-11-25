from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    data_de_ultima_compra= models.DateField()
    quantidade = models.IntegerField()

    def __str__(self):  #definição de função adionada
        return f"{self.nome} - {self.quantidade}" 

class Prato(models.Model):
    nome = models.CharField(max_length=255)
    produtos = models.ManyToManyField(Produto,through='PratoProduto')
    preco = models.FloatField()

    def __str__(self):  #definição de função adionada
        return f"{self.nome} - R${self.preco}" 


class PratoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):  #definição de função adionada
        return f"{self.prato.nome} - {self.produto.nome}" 
