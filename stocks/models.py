from django.db import models


class BSEStocks(models.Model):
    SecurityCode = models.CharField(max_length=1000000)
    Symbol = models.CharField(max_length=20)
    CompanyName = models.CharField(max_length=100)
    Status = models.CharField(max_length=20)
    Group = models.CharField(max_length=5)
    FaceValue = models.CharField(max_length=20)
    IsinNumber = models.CharField(max_length=100)
    Industry = models.CharField(max_length=200)
    Instrument = models.CharField(max_length=200)

    def __str__(self):
        return self.Symbol


class NSEStocks(models.Model):
    Symbol = models.CharField(max_length=20)
    CompanyName = models.CharField(max_length=100)
    Series = models.CharField(max_length=200)
    DateOfListing = models.CharField(max_length=200)
    PaidUpValue = models.CharField(max_length=20)
    MarketLot = models.CharField(max_length=20)
    IsinNumber = models.CharField(max_length=100)
    FaceValue = models.CharField(max_length=20)

    def __str__(self):
        return self.Symbol
