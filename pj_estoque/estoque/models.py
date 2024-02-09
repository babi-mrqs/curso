from django.db import models

# Create your models here.

class Estoque(models.Model):
    nome = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    descricao = models.TextField(blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_att = models.DateTimeField(auto_now=True)

