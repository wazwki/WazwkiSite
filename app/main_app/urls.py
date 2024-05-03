""" Configurate url's for main app """

from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register(r'api/contact', views.ContactViewSet)

urlpatterns = [
    path('', views.index),
    re_path(r'^contact/?$', views.contact),
    re_path(r'^resume/?$', views.resume),
    re_path(r'^about/?$', views.about),
    re_path(r'^git/?$', views.git),
]

urlpatterns += router.urls
