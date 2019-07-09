from django import forms

class Search(forms.Form):
    box=forms.CharField(max_length=20)