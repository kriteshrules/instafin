from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="aceinvestors-home"),
    path('rakesh-jhunjhunwala/', views.rakesh, name="rakesh-jhunjhunwala"),
]