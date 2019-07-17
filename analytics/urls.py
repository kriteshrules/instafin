from django.urls import path
from . import views
from .views import ChartsView, ChartData

urlpatterns = [
    path('', ChartsView.as_view(), name="analytics-home"),
    path('api/chart/data/', ChartData.as_view()),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete_view'),
    path('search/<str:s>/',views.search,name="find")
]