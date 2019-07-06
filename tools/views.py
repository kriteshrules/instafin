from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def toolsHome(request):
    context = {
        'title': 'FinTools',
    }
    return render(request, 'tools/fintools.html', context)
