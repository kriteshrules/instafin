from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import AceInvestor

@login_required
def home(request):
    context = {
        'aceinvestors': AceInvestor.objects.all(),
        'title': 'Ace Investor'
    }
    return render(request, 'aceinvestors/aceinvestors.html', context)

def rakesh(request):
    return render(request, 'aceinvestors/rakesh_jhunjhunwala.html', {'title':'Rakesh Jhunjhunwala'})