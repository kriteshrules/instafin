from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def stocks_home(request):
    return render(request, 'stocks/stock.html', {'title': 'Stocks Home'})


def stock_detail(request):
    quote = request.POST['quote']
    context = {
        'title': 'Stock Detail',
        'quote': quote
    }
    return render(request, 'stocks/stock_detail.html', context)



