from django.db import models


class Thematic(models.Model):
    image = models.CharField(max_length=100)
    theme_name = models.CharField(max_length=100)
    description = models.TextField()
    trend = models.CharField(max_length=200)
    explore = models.CharField(max_length=200)

    def __str__(self):
        return self.theme_name


class DigitalIndia(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class ElectricVehicles(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class EvergreenStocks(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class HalalStocks(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class IncredibleIndia(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class SmartCities(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class SociallyResponsible(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name