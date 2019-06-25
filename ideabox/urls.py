from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="ideabox-home"),
    path('dividend-champions/', views.dividendchampions, name="dividend_champions"),
    path('high-risk-reward/', views.highriskreward, name="highrisk_reward"),
    path('stock-month/', views.stockmonth, name="stock_month"),
    path('top-largecaps/', views.toplargecaps, name="top_largecaps"),
    path('undervalued-stocks/', views.undervaluedstocks, name="undervalued_stocks"),
    path('zero-debt/', views.zerodebt, name="zero_debt"),
]