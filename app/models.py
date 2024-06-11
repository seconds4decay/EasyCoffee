from django.db import models
from django import forms
from django.contrib.auth.models import User



class Cafe(models.Model):
    id_cafe = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, null=False)
    descricao = models.CharField(max_length=1000, null=False)
    tamanho = models.CharField(max_length=120, null=False)
    intensidade = models.CharField(max_length=120, null=False)
    aroma = models.CharField(max_length=120, null=False)
    foto = models.ImageField(upload_to='cafes/')


class Palavra(models.Model):
    palavra = models.CharField(max_length=100, unique=True)
    significado = models.TextField()

class favoritar(models.Model):
    user = models.CharField(max_length=100, null=False)
    cafe = models.IntegerField(default=0)