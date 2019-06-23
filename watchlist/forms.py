from django import forms
from .models import WatchList


class WatchlistForm(forms.ModelForm):
    stock_name = forms.CharField(max_length=100)
    target_price = forms.FloatField()
    comment = forms.CharField(max_length=2000)

    class Meta:
        model = WatchList
        fields = ['stock_name', 'target_price', 'comment']

