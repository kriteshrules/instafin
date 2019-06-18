from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def stocks_home(request):
    return render(request, 'stocks/stock.html', {'title': 'Stocks Home'})


def stock_detail(request):
    return  render(request, 'stocks/stock_detail.html', {'title': 'Stock Detail'})