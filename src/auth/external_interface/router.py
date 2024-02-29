from django.urls import path

from auth.external_interface import controllers

urlpatterns = [
    path('clients/', controllers.register_client),
]
