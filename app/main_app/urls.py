""" Configurate url's for main app """

from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^contact/?$', views.contact),
    re_path(r'^resume/?$', views.resume),
    re_path(r'^about/?$', views.about),
]
