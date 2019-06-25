from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BSEStocks, NSEStocks


def stocks_home(request):
    context = {
        'BSEStocks': BSEStocks.objects.all(),
        'NSEStocks': NSEStocks.objects.all(),
        'title': 'Stocks Home'
    }
    return render(request, 'stocks/stock.html', context)


def stock_detail(request):
    quote = request.POST['quote']
    context = {
        'title': 'Stock Detail',
        'quote': quote
    }
    return render(request, 'stocks/stock_detail.html', context)



