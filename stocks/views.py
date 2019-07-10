from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BSEStocks, NSEStocks
from sentiment.googlesentiment import Analysis
from sentiment.sentimeter import TwitterSentiment
from django.db.models import Q
from . import forms
import json
from django.http import HttpResponse


def stocks_home(request):
    context = {
        'BSEStocks': BSEStocks.objects.all(),
        'NSEStocks': NSEStocks.objects.all(),
        'title': 'Stocks Home'
    }
    return render(request, 'stocks/stock.html', context)


def stock_detail(request):
    if request.method == "POST":
        quote = request.POST['quote']
    term = quote
    keyword = quote
    analysis = Analysis(term)
    analysis.run()
    twittersentiment = TwitterSentiment(keyword)
    twittersentiment.run()
    context = {
        'title': 'Stock Detail',
        'quote': quote,
        "Term": term,
        "Sentiment": analysis.sentiment,
        "Subjectivity": analysis.subjectivity,
        "gheadline_pos": analysis.gheadline_pos,
        "gheadline_neu": analysis.gheadline_neu,
        "gheadline_neg": analysis.gheadline_neg,
        "pos_count": analysis.pos_count,
        "neg_count": analysis.neg_count,
        "neu_count": analysis.neu_count,
        "headings": analysis.headings,
        "urls": analysis.urls,
        "mylist": analysis.mylist,              #list of news
        "newtweetn": twittersentiment.newtweetn,
        "newtweetp": twittersentiment.newtweetp,
        'pos_countt': twittersentiment.pos_count,
        'neg_countt': twittersentiment.neg_count,
        'neutral_count': twittersentiment.neutral_count,
        'keyword': keyword,
    }
    return render(request, 'stocks/stock_detail.html', context)


def stocks_search(request):
    form = forms.Search()
    context = {
        'NSEStocks': NSEStocks.objects.all(),
        'title': 'Stocks Search',
        'form': form
    }
    return render(request, 'stocks/stock_search.html', context)


def search(request,s):
    res = []
    try:
        q= NSEStocks.objects.filter( Q(Symbol__istartswith=s ) )
        for i in q:
            s=s.upper()
            Symbol=i.Symbol.capitalize()
            if( Symbol.startswith(s) ):
                res.append(Symbol)
        print(res)

    except Exception as e:
        print("Error",e)

    return HttpResponse(json.dumps({"res":res}),content_type="application/json")
