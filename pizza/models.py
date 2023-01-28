from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=6)
    def __str__(self):
        return self.title


class Topping(models.Model):
    title =  models.CharField(max_length=10)
    def __str__(self):
        return self.title


class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping)

    def __str__(self):
        return f'{self.size}'
