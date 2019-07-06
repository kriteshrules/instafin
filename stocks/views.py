from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BSEStocks, NSEStocks
from sentiment.googlesentiment import Analysis
from sentiment.sentimeter import TwitterSentiment
from .models import BSEStocks


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
        "newtweetn": twittersentiment.newtweetn,
        "newtweetp": twittersentiment.newtweetp,
        'pos_countt': twittersentiment.pos_count,
        'neg_countt': twittersentiment.neg_count,
        'neutral_count': twittersentiment.neutral_count,
        'keyword': keyword,
    }
    return render(request, 'stocks/stock_detail.html', context)
