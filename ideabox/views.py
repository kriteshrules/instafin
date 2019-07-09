from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ideabox, DividendChampions, HighRiskReward, StockMonth, TopLargecaps, UndervaluedStocks, ZeroDebt
from stocks.stockquote import getQuotes


@login_required
def home(request):
    context = {
        'ideabox': Ideabox.objects.all(),
        'title': 'Ideabox'
    }
    return render(request, 'ideabox/ideabox.html', context)


def zerodebt(request):
    symbol = ZeroDebt.objects.values_list('stock_name', flat=True)
    comment = ZeroDebt.objects.values_list('comment', flat=True)

    q = getQuotes(symbol)
    q.run()

    mylist = zip(symbol, q.stocknamelist, q.closepricelist, comment)

    context = {
        'zerodebt': ZeroDebt.objects.all(),
        'title': 'Zero debt stocks',
        'mylist': mylist,
    }
    return render(request, 'ideabox/zero_debt.html', context)


def dividendchampions(request):
    context = {
        'dividendchampions': DividendChampions.objects.all(),
        'title': 'Dividend Champions'
    }
    return render(request, 'ideabox/dividend_champions.html', context)


def highriskreward(request):
    context = {
        'highriskreward': HighRiskReward.objects.all(),
        'title': 'High Risk, High Reward'
    }
    return render(request, 'ideabox/highrisk_reward.html', context)


def stockmonth(request):
    context = {
        'stockmonth': StockMonth.objects.all(),
        'title': 'Stock of the month'
    }
    return render(request, 'ideabox/stock_month.html', context)


def toplargecaps(request):
    context = {
        'toplargecaps': TopLargecaps.objects.all(),
        'title': 'Top 1% Largecap stocks'
    }
    return render(request, 'ideabox/top_largecaps.html', context)


def undervaluedstocks(request):
    context = {
        'undervaluedstocks': UndervaluedStocks.objects.all(),
        'title': 'Undervalued stocks'
    }
    return render(request, 'ideabox/undervalued_stocks.html', context)