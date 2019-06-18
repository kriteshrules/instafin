from django.urls import path
from . import views

urlpatterns = [
    path('', views.fijourney_home, name="fijourney-home"),
    path('result', views.result, name='fi-result'),

]