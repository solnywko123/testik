from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

class Establishment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    places = models.IntegerField()
    hours_of_operation = models.CharField(max_length=255)
    requirements = models.TextField()
