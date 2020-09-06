from django.db import models
#from django.contrib.auth.models import User


class User(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.login


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, blank=True, related_name="orders")
    orderer_id = models.IntegerField()
    total = models.FloatField()
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return f"done #{self.id}"
        return f"order #{self.id}"
