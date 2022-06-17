from django.db import models

# Create your models here.

class Colors(models.Model):
    color_id=models.BigAutoField(primary_key=True)
    name = models.TextField( blank=False,unique = True)

class Countries (models.Model):
    country_id=models.BigAutoField(primary_key=True)
    name = models.TextField( blank=False,unique = True)

class Descriptions (models.Model):
    description_id=models.BigAutoField(primary_key=True)
    description = models.TextField(blank=False,unique = True)

class Teas (models.Model):
    tea_id=models.BigAutoField(primary_key=True)
    name = models.TextField( blank=False,unique = True)
    color = models.ForeignKey(Colors, null=True, on_delete = models.SET_NULL)
    description = models.OneToOneField(Descriptions, null=True, on_delete = models.CASCADE)
    countries = models.ManyToManyField(Countries)
