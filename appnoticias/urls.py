"""noticias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

"""
#####URLS APPNOTICIAS #####

from django.urls import path
from appnoticias.views import ListaNoticias

urlpatterns = [
    path('appnoticias/', ListaNoticias.as_view(), name='appnoticias'),
    path('noticia/<int:noticia>', ListaNoticias.as_view(), name='noticia'),
    path('scra_noticias/', ListaNoticias.scrapring),
]
