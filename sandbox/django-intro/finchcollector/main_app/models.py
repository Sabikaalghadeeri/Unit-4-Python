from django.db import models

# Create your models here.

class Finch(models.Model):
    scientific_name = models.CharField(max_length=100)
    bird_family = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    key_information = models.TextField(max_length=250)
    weight = models.IntegerField()
    
    def __str__(self):
        return self.scientific_name