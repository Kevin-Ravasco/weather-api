from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Yoyogroup Weather API",
        default_version='v1',
        description="API documentation for our weather endpoints. "
                    "Find all information related to the routes included in Vault"
                    " under this document."
                    "\n\nThe `swagger-ui` view can be found [here](/)."
                    "\n\nThe `ReDoc` view can be found [here](redoc/). ",

        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="okevin182@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # SWAGGER UI patterns
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
