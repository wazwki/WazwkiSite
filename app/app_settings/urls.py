"""
URL configuration for app_setings project.
"""

from django.contrib import admin
from django.urls import path, re_path, include
from main_app.views import page_not_found

urlpatterns = [
    re_path(r'^admin/?', admin.site.urls),
    path('', include('main_app.urls')),
]

handler404 = page_not_found