from rest_framework import serializers


class AddClientRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    description = serializers.CharField()


class AddClientResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    date_joined = serializers.DateTimeField()
    last_login = serializers.DateTimeField(allow_null=True)
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
