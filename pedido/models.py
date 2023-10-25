from django.db import models
from django.contrib.auth.models import User
from estoque.models import Prato


# Create your models here.
class Pedido(models.Model):
    usuario: models.ForeignKey(User, on_delete=models.CASCADE)
    prato: models.ForeignKey(Prato, on_delete=models.PROTECT)
    datahora: models.DateTimeField()
