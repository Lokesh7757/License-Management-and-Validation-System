# license_validator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.validate_license, name='validate_license'),
]
