from django.db import models

# Create your models here.

class Person(models.Model):
	primeiroNome = models.CharField(max_length=30)
	ultimoNome = models.CharField(max_length=30)
	
class Perfils(models.Model):
	nome=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	telefone=models.CharField(max_length=30)