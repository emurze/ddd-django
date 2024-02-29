from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from auth.external_interface.serializers import \
    RegistrationRequestSerializer, RegistrationResponseSerializer
from shared.external_interface.serializers import FailedSerializer


@extend_schema(
    tags=["clients"],
    request=RegistrationRequestSerializer,
    parameters=[
        OpenApiParameter(
            location=OpenApiParameter.QUERY,
            name="name",
            type=str,
            required=False,
        ),
    ],
    responses={
        status.HTTP_201_CREATED: RegistrationResponseSerializer,
        status.HTTP_400_BAD_REQUEST: FailedSerializer,
    }
)
@api_view(['POST'])
def register_client(request: Request):
    serializer = RegistrationRequestSerializer(data=request.data)

    if serializer.is_valid():
        print(serializer.data)
    else:
        return Response(
            {"detail": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response("hello world")
