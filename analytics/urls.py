from django.urls import path
from . import views
from .views import ChartsView, ChartData

urlpatterns = [
    path('', ChartsView.as_view(), name="analytics-home"),
    path('api/chart/data/', ChartData.as_view())
]