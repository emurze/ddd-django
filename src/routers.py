from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Login
    path('login/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('login/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
