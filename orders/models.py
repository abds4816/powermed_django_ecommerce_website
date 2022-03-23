from django.contrib.admin.sites import site
from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    details = models.ManyToManyField(Product, through='OrderItem')
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return 'order: '+ str(self.id) + ', user: ' + self.first_name

    def get_total_cost(self):
    	return sum(item.get_cost() for item in self.items.all())

    class Meta:
        ordering = ['-order_date']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return 'Product: ' + self.product.name + ', Order: ' + str(self.order.id)

    def get_cost(self): 
        return self.price * self.quantity