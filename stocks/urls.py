from django.urls import path
from . import views

urlpatterns = [
    path('', views.stocks_home, name="stocks-home"),
    path('stock-detail/', views.stock_detail, name='stock-detail'),
    path('stock-search/', views.stocks_search, name='stock-search'),
    path('stock-search/search/<str:s>/',views.search,name="find")
]