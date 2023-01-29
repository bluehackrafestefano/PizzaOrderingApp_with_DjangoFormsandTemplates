from django.db import models
from django.contrib.auth.models import User


class Size(models.Model):
    name = models.CharField(max_length=6)
    def __str__(self):
        return self.name


class Topping(models.Model):
    name =  models.CharField(max_length=10)
    topping_price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name


class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping)
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    pizza_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        toppings = ', '.join(str(v) for v in self.topping.all())
        return f'{self.size.name} - {toppings} - {self.customer_name} - {self.address} - {self.pizza_price}'
