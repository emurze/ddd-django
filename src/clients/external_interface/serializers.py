from rest_framework import serializers

from clients.domain.entities import Client


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
