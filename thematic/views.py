from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Thematic, DigitalIndia, ElectricVehicles, EvergreenStocks, HalalStocks, IncredibleIndia, SmartCities, SociallyResponsible



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
    context = {
        'electricvehicles': ElectricVehicles.objects.all(),
        'title': 'Electric Vehicles'
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