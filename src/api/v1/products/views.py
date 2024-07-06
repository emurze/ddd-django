from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.v1.products.filters import ProductFilter
from api.v1.products.serializers import ProductSerializer
from apps.products.models import Product
from project.containers import get_mediator


class ProductReadViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    ordering_fields = [
        "title",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    mediator = get_mediator()

    def post(self, request: Request, *args) -> Response:
        self.mediator.handle()

    # def put(self, request: Request, *args) -> Response:
    #     return Response({"detail": {"error": "Not Implemented"}})
    #
    # def delete(self, request: Request, *args) -> Response:
    #     return Response({"detail": {"error": "Not Implemented"}})
