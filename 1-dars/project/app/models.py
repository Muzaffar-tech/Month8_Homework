from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    color = models.ForeignKey(Color, models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, models.SET_NULL, null=True)
    year = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
