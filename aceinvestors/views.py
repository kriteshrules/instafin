from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AceInvestor, RakeshJhunjhnwalaPortfolio, DollyKhanna, AkashBhanshali, AnilKumarGoel, AshishKacholia, MohnishPabrai, NemishShah, VijayKedia


@login_required
def home(request):
    context = {
        'aceinvestors': AceInvestor.objects.all(),
        'title': 'Ace Investor'
    }
    return render(request, 'aceinvestors/aceinvestors.html', context)


def rakesh(request):
    context = {
        'rjp': RakeshJhunjhnwalaPortfolio.objects.all(),
        'title': 'Rakesh Jhunjhunwala'
    }
    return render(request, 'aceinvestors/rakesh_jhunjhunwala.html', context)


def dollykhanna(request):
    context = {
        'dollykhanna': DollyKhanna.objects.all(),
        'title': 'Dolly Khanna'
    }
    return render(request, 'aceinvestors/DollyKhanna.html', context)


def akashbhanshali(request):
    context = {
        'akashbhanshali': AkashBhanshali.objects.all(),
        'title': 'Akash Bhanshali'
    }
    return render(request, 'aceinvestors/AkashBhanshali.html', context)


def anilkumargoel(request):
    context = {
        'anilkumargoel': AnilKumarGoel.objects.all(),
        'title': 'Anil Kumar Goel'
    }
    return render(request, 'aceinvestors/AnilKumarGoel.html', context)


def ashishkacholia(request):
    context = {
        'ashishkacholia': AshishKacholia.objects.all(),
        'title': 'Ashish Kacholia'
    }
    return render(request, 'aceinvestors/AshishKacholia.html', context)


def mohnishpabrai(request):
    context = {
        'mohnishpabrai': MohnishPabrai.objects.all(),
        'title': 'Mohnish Pabrai'
    }
    return render(request, 'aceinvestors/MohnishPabrai.html', context)


def nemishshah(request):
    context = {
        'nemishshah': NemishShah.objects.all(),
        'title': 'Nemish Shah'
    }
    return render(request, 'aceinvestors/NemishShah.html', context)


def vijaykedia(request):
    context = {
        'vijaykedia': VijayKedia.objects.all(),
        'title': 'Vijay Kedia'
    }
    return render(request, 'aceinvestors/VijayKedia.html', context)

