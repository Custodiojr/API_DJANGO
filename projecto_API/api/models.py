from django.db import models

#Criar tabelas
class Company(models.Model):
    name=models.CharField(max_length=50)
    website=models.URLField(max_length=100)
    foundation=models.PositiveIntegerField()
