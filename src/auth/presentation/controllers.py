from collections.abc import Callable

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from auth.application import dtos as d
from auth.presentation import serializers as s
from auth.presentation.container import add_client_uc_factory


# Place for FastAPI and place for Django


@extend_schema(
    tags=["clients"],
    request=s.AddClientRequestSerializer,
    responses={
        status.HTTP_201_CREATED: s.AddClientResponseSerializer,
    }
)
@api_view(['POST'])
def add_client(
    request: Request,
    get_use_case: Callable = add_client_uc_factory,
):
    request_dto = s.AddClientRequestSerializer(data=request.data)
    if not request_dto.is_valid():
        return Response(request_dto.errors)

    use_case = get_use_case()
    intput_dto = d.AddClientInputDto(**request_dto.data)
    output_dto = use_case.execute(intput_dto)

    response = s.AddClientResponseSerializer(data=output_dto.model_dump())
    if not response.is_valid():
        return Response(response.errors)

    return Response(response.data)

# @extend_schema(
#     tags=["clients"],
#     request=RegistrationRequestSerializer,
#     parameters=[
#         OpenApiParameter(
#             location=OpenApiParameter.QUERY,
#             name="name",
#             type=str,
#             required=False,
#         ),
#     ],
#     responses={
#         status.HTTP_201_CREATED: RegistrationResponseSerializer,
#         status.HTTP_400_BAD_REQUEST: FailedSerializer,
#     }
# )
# @api_view(['POST'])
# def register_client(request: Request):
#     serializer = RegistrationRequestSerializer(data=request.data)
#
#     if serializer.is_valid():
#         print(serializer.data)
#     else:
#         return Response(
#             {"detail": serializer.errors},
#             status=status.HTTP_400_BAD_REQUEST,
#         )
#
#     return Response("hello world")
