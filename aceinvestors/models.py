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


class BulkDeals(models.Model):
    deal_date = models.CharField(max_length=100)
    security_code = models.CharField(max_length=1000000)
    company_symbol = models.CharField(max_length=20)
    client_name = models.CharField(max_length=100)
    deal_type = models.CharField(max_length=2)
    quantity = models.CharField(max_length=1000000)
    price= models.FloatField()

    def __str__(self):
        return self.company_symbol


#Investors portfolio model starts here

class RakeshJhunjhnwalaPortfolio(models.Model):
    company_name = models.CharField(max_length=100)
    company_symbol = models.CharField(max_length=100)
    total_quantity_held = models.CharField(max_length=100)
    Holding_percent = models.CharField(max_length=100)
    Change_last_quarter = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class AkashBhanshali(models.Model):
    company_name = models.CharField(max_length=100)
    company_symbol = models.CharField(max_length=100)
    total_quantity_held = models.CharField(max_length=100)
    Holding_percent = models.CharField(max_length=100)
    Change_last_quarter = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class AnilKumarGoel(models.Model):
    company_name = models.CharField(max_length=100)
    company_symbol = models.CharField(max_length=100)
    total_quantity_held = models.CharField(max_length=100)
    Holding_percent = models.CharField(max_length=100)
    Change_last_quarter = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class AshishKacholia(models.Model):
    company_name = models.CharField(max_length=100)
    company_symbol = models.CharField(max_length=100)
    total_quantity_held = models.CharField(max_length=100)
    Holding_percent = models.CharField(max_length=100)
    Change_last_quarter = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class DollyKhanna(models.Model):
    company_name = models.CharField(max_length=100)
    company_symbol = models.CharField(max_length=100)
    total_quantity_held = models.CharField(max_length=100)
    Holding_percent = models.CharField(max_length=100)
    Change_last_quarter = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class MohnishPabrai(models.Model):
    company_name = models.CharField(max_length=100)
    company_symbol = models.CharField(max_length=100)
    total_quantity_held = models.CharField(max_length=100)
    Holding_percent = models.CharField(max_length=100)
    Change_last_quarter = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class NemishShah(models.Model):
    company_name = models.CharField(max_length=100)
    company_symbol = models.CharField(max_length=100)
    total_quantity_held = models.CharField(max_length=100)
    Holding_percent = models.CharField(max_length=100)
    Change_last_quarter = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class VijayKedia(models.Model):
    company_name = models.CharField(max_length=100)
    company_symbol = models.CharField(max_length=100)
    total_quantity_held = models.CharField(max_length=100)
    Holding_percent = models.CharField(max_length=100)
    Change_last_quarter = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name





