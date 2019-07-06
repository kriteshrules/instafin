from django.urls import path
from . import views

urlpatterns = [
    path('', views.toolsHome, name="tools-home"),

]