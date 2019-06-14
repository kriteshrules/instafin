from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="aceinvestors-home"),
    path('add', views.add, name="add")
]