from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="thematic-home"),
    path('digital-india/', views.digitalindia, name="digital_india"),
    path('electric-vehicles/', views.electricvehicles, name="electric_vehicles"),
    path('evergreen-stocks/', views.evergreenstocks, name="evergreen_stocks"),
    path('halal-stocks/', views.halalstocks, name="halal_stocks"),
    path('incredible-india/', views.incredibleindia, name="incredible_india"),
    path('smart-cities/', views.smartcities, name="smart_cities"),
    path('socially-responsible/', views.sociallyresponsible, name="socially_responsible"),
]