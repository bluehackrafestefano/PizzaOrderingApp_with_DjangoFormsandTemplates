from django.db import models
from django.contrib.auth.models import User


class Size(models.Model):
    name = models.CharField(max_length=6)
    def __str__(self):
        return self.name


class Topping(models.Model):
    name =  models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping)

    def __str__(self):
        return self.size


class Order(models.Model):
    pizza = models.OneToOneField(Pizza, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    # customer = models.ForeignKey(
    #     User, 
    #     null=True, 
    #     on_delete=models.CASCADE, 
    #     related_name='orders'
    # )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now=True)
    # in_cart = models.BooleanField(default=True)
    # placed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
