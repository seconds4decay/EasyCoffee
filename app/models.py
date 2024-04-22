from django.db import models

class Cafe(models.Model):
    id_cafe = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, null=False)
    descricao = models.CharField(max_length=1000, null=False)

class Palavra(models.Model):
    palavra = models.CharField(max_length=100, unique=True)
    significado = models.TextField()
