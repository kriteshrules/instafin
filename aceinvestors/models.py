from django.db import models

# Create your models here.


class AceInvestor(models.Model):
    investor_name = models.CharField(max_length=100)
    stock_no = models.CharField(max_length=100)
    investor_summary = models.TextField()
    profile_link = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)

    def __str__(self):
        return self.investor_name



