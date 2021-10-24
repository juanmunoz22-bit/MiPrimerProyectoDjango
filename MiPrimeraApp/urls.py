from django.urls import path

from MiPrimeraApp import views

urlpatterns = [

    path('', views.home, name='home'),
]
