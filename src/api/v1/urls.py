from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.products.views import ProductReadViewSet

main_router = DefaultRouter()
main_router.register("products", ProductReadViewSet)

urlpatterns = [
    path("", include(main_router.urls)),
]
