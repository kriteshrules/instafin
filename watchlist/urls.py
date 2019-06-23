from django.urls import path
from . import views
from .views import StockListView

urlpatterns = [
    path('', StockListView.as_view(), name="watchlist-home"),
]