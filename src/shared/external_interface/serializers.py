from rest_framework import serializers


class FailedSerializer(serializers.Serializer):
    detail = serializers.CharField()
