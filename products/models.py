from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='categories/%Y/%m/%d')

    def __str__(self):
        return self.category_name

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    brand = models.CharField(max_length=150)
    ability = models.IntegerField()
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name