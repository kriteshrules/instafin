from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Thematic, DigitalIndia, ElectricVehicles, EvergreenStocks, HalalStocks, IncredibleIndia, SmartCities, SociallyResponsible
from sentiment.googlesentiment import Analysis
from sentiment.sentimeter import TwitterSentiment


@login_required
def home(request):
    context = {
        'thematic': Thematic.objects.all(),
        'title': 'Thematic Investments'
    }
    return render(request, 'thematic/thematic.html', context)


def digitalindia(request):
    context = {
        'digitalindia': DigitalIndia.objects.all(),
        'title': 'Digital India'
    }
    return render(request, 'thematic/digital_india.html', context)


def electricvehicles(request):
    term = 'Electric+vehicles'
    analysis = Analysis(term)
    analysis.run()
    keyword = 'electricvehicle'
    twittersentiment = TwitterSentiment(keyword)
    twittersentiment.run()
    context = {
        'electricvehicles': ElectricVehicles.objects.all(),
        'title': 'Electric Vehicles',
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
    return render(request, 'thematic/electric_vehicles.html', context)


def evergreenstocks(request):
    context = {
        'evergreenstocks': EvergreenStocks.objects.all(),
        'title': 'Evergreen Stocks'
    }
    return render(request, 'thematic/evergreen_stocks.html', context)


def halalstocks(request):
    context = {
        'halalstocks': HalalStocks.objects.all(),
        'title': 'HalalStocks'
    }
    return render(request, 'thematic/halal_stocks.html', context)


def incredibleindia(request):
    context = {
        'incredibleindia': IncredibleIndia.objects.all(),
        'title': 'Incredible India'
    }
    return render(request, 'thematic/incredible_india.html', context)


def smartcities(request):
    context = {
        'smartcities': SmartCities.objects.all(),
        'title': 'Smart Cities'
    }
    return render(request, 'thematic/smart_cities.html', context)


def sociallyresponsible(request):
    context = {
        'sociallyresponsible': SociallyResponsible.objects.all(),
        'title': 'Socially Responsible'
    }
    return render(request, 'thematic/socially_responsible.html', context)