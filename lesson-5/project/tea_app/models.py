from django.db import models

# Create your models here.

class Colors(models.Model):
    color_id=models.BigAutoField(primary_key=True)
    name = models.TextField( blank=False,unique = True)

    class Meta:
        ordering = ['color_id']


class Teas (models.Model):
    tea_id=models.BigAutoField(primary_key=True)
    name = models.TextField( blank=False,unique = True)
    description = models.TextField(null = True, blank=True)
    color = models.ForeignKey(Colors, null=True, on_delete = models.SET_NULL)
    countries = models.TextField(null = True, blank=True)

    class Meta:
        ordering = ['tea_id']

