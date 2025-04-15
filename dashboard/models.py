from django.db import models

class VendaMensal(models.Model):
    mes = models.CharField(max_length=10)
    valor = models.FloatField()

class VendaCategoria(models.Model):
    categoria = models.CharField(max_length=50)
    valor = models.FloatField()

class ClienteRegiao(models.Model):
    regiao = models.CharField(max_length=50)
    quantidade = models.IntegerField()