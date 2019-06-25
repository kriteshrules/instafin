from django.db import models


class Ideabox(models.Model):
    image = models.CharField(max_length=100)
    idea_name = models.CharField(max_length=100)
    stock_no = models.CharField(max_length=100)
    description = models.TextField()
    explore = models.CharField(max_length=200)

    def __str__(self):
        return self.idea_name


class DividendChampions(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class HighRiskReward(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class StockMonth(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class TopLargecaps(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class UndervaluedStocks(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name


class ZeroDebt(models.Model):
    stock_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.stock_name

