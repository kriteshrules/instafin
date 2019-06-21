from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    import requests
    import json
    api_request = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=96f2ee30b88e4e6fb678f5a4192edfab')
    api = json.loads(api_request.content)
    return render(request, 'dashboard/dashboard.html', {'api': api})


#'title': 'Dashboard'