from django.urls import path
from django.contrib import admin
from . import views
from . import myroute


urlpatterns = [
    path('', views.home, name='home'),
    path('myroute', myroute.myroute, name='myroute'),
    path('another', views.myAnotherRoute, name='another'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]