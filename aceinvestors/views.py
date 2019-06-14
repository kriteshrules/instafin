from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import AceInvestor

aceinvestors = [
    {
        'investor_name': 'Rakesh Jhunjhunwala',
        'stock_no': '16',
        'investor_summary': 'Cras sit amet nibh libero, in gravida nulla',
        'profile_link': 'abx.yzp'
    },
    {
        'investor_name': 'Mohnish Pabrai',
        'stock_no': '9',
        'investor_summary': 'Cras sit amet nibh libero, in gravida nulla',
        'profile_link': 'abx.yzp'
    },
    {
        'investor_name': 'Dolly Khanna',
        'stock_no': '26',
        'investor_summary': 'Cras sit amet nibh libero, in gravida nulla',
        'profile_link': 'abx.yzp'
    }
]

@login_required
def home(request):
    context = {
        'aceinvestors': AceInvestor.objects.all(),
        'title': 'Ace Investor'
    }
    return render(request, 'aceinvestors/aceinvestors.html', context)

def rakesh(request):
    return render(request, 'aceinvestors/rakesh_jhunjhunwala.html', {'title':'Rakesh Jhunjhunwala'})