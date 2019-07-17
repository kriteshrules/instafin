from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    stock_name = models.CharField(max_length=100)
    purchase_price = models.FloatField()
    purchase_quantity = models.BigIntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.stock_name