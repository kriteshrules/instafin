from django.db import models
from django.contrib.auth.models import User


class WatchList(models.Model):
    stock_name = models.CharField(max_length=100)
    target_price = models.FloatField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.stock_name