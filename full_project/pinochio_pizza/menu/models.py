from django.db import models


class Regular_Pizza(models.Model):
    name = models.CharField(max_length=64)
    small = models.FloatField()
    large = models.FloatField()
    topping_quantity = models.IntegerField()
    image = models.CharField(max_length=86, default="menu/images/default.jpg")

    def __str__(self):
        return f"{self.name} Regular id:{self.id}"


class Sicilian_Pizza(models.Model):
    name = models.CharField(max_length=64)
    small = models.FloatField()
    large = models.FloatField()
    topping_quantity = models.IntegerField()
    image = models.CharField(max_length=86, default="menu/images/default.jpg")

    def __str__(self):
        return f"{self.name} Sicilian {self.id}"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"



class Sub(models.Model):
    name = models.CharField(max_length=64)
    small = models.FloatField()
    large = models.FloatField()
    image = models.CharField(max_length=86, default="menu/images/default.jpg")

    def __str__(self):
        return self.name


class Extra_Sub(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    image = models.CharField(max_length=86, default="menu/images/default.jpg")

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    image = models.CharField(max_length=86, default="menu/images/default.jpg")

    def __str__(self):
        return self.name


class Dinner_Platter(models.Model):
    name = models.CharField(max_length=64)
    small = models.FloatField()
    large = models.FloatField()
    image = models.CharField(max_length=86, default="menu/images/default.jpg")

    def __str__(self):
        return self.name
