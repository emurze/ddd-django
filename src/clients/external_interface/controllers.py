from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from clients.domain.entities import Client


class ClientRegistration(CreateAPIView):
    model = Client
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
