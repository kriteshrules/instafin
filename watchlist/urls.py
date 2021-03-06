from django.urls import path
from . import views
from .views import StockListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(StockListView.as_view()), name="watchlist-home"),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete_view'),
    path('find/<str:s>/',views.find,name="find")
]