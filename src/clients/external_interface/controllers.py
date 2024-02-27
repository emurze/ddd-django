from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from clients.domain.entities import Client
from clients.external_interface.serializers import RegistrationSerializer


class ClientRegistration(CreateAPIView):
    model = Client
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
