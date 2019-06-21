from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="aceinvestors-home"),
    path('rakesh-jhunjhunwala/', views.rakesh, name="rakesh-jhunjhunwala"),
    path('dolly-khanna/', views.dollykhanna, name="dolly-khanna"),
    path('akash-bhanshali/', views.akashbhanshali, name="akash-bhanshali"),
    path('anil-kumar-goel/', views.anilkumargoel, name="anil-kumar-goel"),
    path('ashish-kacholia/', views.ashishkacholia, name="ashish-kacholia"),
    path('mohnish-pabrai/', views.mohnishpabrai, name="mohnish-pabrai"),
    path('nemish-shah/', views.nemishshah, name="nemish-shah"),
    path('vijay-kedia/', views.vijaykedia, name="vijay-kedia"),

]