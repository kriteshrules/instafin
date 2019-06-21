from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Thematic


@login_required
def home(request):
    context = {
        'thematic': Thematic.objects.all(),
        'title': 'Thematic Investments'
    }
    return render(request, 'thematic/thematic.html', context)