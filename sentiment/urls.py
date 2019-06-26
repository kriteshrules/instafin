from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="sentiment-home"),
    path('sentiment', views.sentiment, name="sentiment"),
    path('googlesentiment', views.googlesentiment, name="google_sentiment")
]