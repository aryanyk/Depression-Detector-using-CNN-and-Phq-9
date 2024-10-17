# create url patterns for the home page and the about page
# """
# URL configuration for app application.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# """
#
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("assesment/", views.phq9_view, name="phq9"),
    
]



