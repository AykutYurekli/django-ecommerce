from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_name = models.CharField(max_length=100, default='placeholder.png')
    color = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name
    


