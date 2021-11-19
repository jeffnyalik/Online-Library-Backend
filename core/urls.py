from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Online Library Management',
        default_version='v1',
        description="Library Management System",
        contact=openapi.Contact(email="jeffnyak@gmail.com"),
        license=openapi.License(name="Library Organization"),
    ),
    public=True,
    permission_classes = (permissions.AllowAny,)
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
         
    path('', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'), 

    path('admin/', admin.site.urls),
    path('api/catalog/', include('catalog.urls'), name='catalog-app'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)