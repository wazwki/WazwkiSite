""" Configurate url's for main app """

from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from . import views
from . import api

router = SimpleRouter()

router.register(r'api/contact', api.ContactViewSet)

urlpatterns = [
    path('', views.index),
    re_path(r'^contact/?$', views.contact),
    re_path(r'^resume/?$', views.resume),
    re_path(r'^about/?$', views.about),
]

urlpatterns += router.urls
