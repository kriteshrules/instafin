from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class ChartsView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Analytics '
        }
        return render(request, 'analytics/chartshome.html', context)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        defaultLabels = ["March", "April", "May", "June", "July"]
        defaultData = [4, 7, 8, 6, 9]
        sectors = ["Auto", "IT", "Pharma", "Banks", "Metals"]
        sectorsData = [5, 7, 3, 8, 2]
        holdings = ["HUL", "Infosys", "Vedanta", "HDFC Bank", "Maruti"]
        holdingsPercent = [28, 13, 12, 8, 7]
        data = {
            "defaultLabels": defaultLabels,
            "defaultData": defaultData,
            "sectors": sectors,
            "sectorsData": sectorsData,
            "holdings": holdings,
            "holdingsPercent": holdingsPercent,
        }
        return Response(data)