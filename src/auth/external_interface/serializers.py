from django.contrib.auth import get_user_model
from rest_framework import serializers

ClientModel = get_user_model()


class RegistrationRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class RegistrationResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'
