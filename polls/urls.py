from django.urls import path

from . import views
from . import myroute

urlpatterns = [
    path('', views.index, name='index'),
    path('myroute/', myroute.myroute, name='myroute'),
    path('another/', views.myanotherroute, name='another'),
    path('home/', views.home, name='home'),
]