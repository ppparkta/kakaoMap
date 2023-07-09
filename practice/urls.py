
from django.contrib import admin
from django.urls import path, include
from practice.views import map_view, save_marker_view

urlpatterns = [
    path('map/', map_view, name='map'),
    path('map/save_marker/', save_marker_view, name='save_marker'),
]
