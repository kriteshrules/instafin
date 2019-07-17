from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    stock_name = forms.CharField(max_length=100)
    purchase_price = forms.FloatField()
    purchase_quantity = forms.IntegerField(max_value=10000000)
    comment = forms.CharField(max_length=2000)

    class Meta:
        model = Portfolio
        fields = ['stock_name', 'purchase_price', 'purchase_quantity', 'comment']