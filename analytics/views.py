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
        defaultLabels = ["Feb", "March", "April", "May", "June", "July"]
        defaultData = [-0.7,2.2, -0.4, 1.5, 3.2, 1.3]
        sectors = ["Auto", "IT", "Pharma", "Banks", "Metals", "Energy", "Oil & Petro"]
        sectorsData = [15, 10, 8, 35, 15, 5, 12]
        holdings = ["HUL", "Infosys", "Vedanta", "HDFC Bank", "Maruti"]
        holdingsPercent = [28, 13, 12, 8, 7]
        stocklist = ["HUL", "Infosys", "Vedanta", "HDFC Bank", "Maruti", "HPCL", "Tata Steel"]
        positivesent = [0.7, 0.6, 0.9, 0.8, 0.5, 0.4, 0.7]
        negativesent = [0.3, 0.4, 0.1, 0.2, 0.5, 0.6, 0.3]

        data = {
            "defaultLabels": defaultLabels,
            "defaultData": defaultData,
            "sectors": sectors,
            "sectorsData": sectorsData,
            "holdings": holdings,
            "holdingsPercent": holdingsPercent,
            "stocklist": stocklist,
            "positivesent": positivesent,
            "negativesent": negativesent
        }
        return Response(data)