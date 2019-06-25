from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ideabox

@login_required
def home(request):
    context = {
        'ideabox': Ideabox.objects.all(),
        'title': 'Ideabox'
    }
    return render(request, 'ideabox/ideabox.html', context)