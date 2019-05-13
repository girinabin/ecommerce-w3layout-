from django.db import models

# Create your models here.

class Nut(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    discount = models.IntegerField()


class Oil(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    discount = models.IntegerField()

class Pasta_Noodle(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    discount = models.IntegerField()
