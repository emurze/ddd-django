from django.urls import path

from auth.presentation import controllers

urlpatterns = [
    path('clients/', controllers.add_client),
]
