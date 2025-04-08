"""{{ cookiecutter.project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import include, path
{%- if cookiecutter.use_drf == "y" %}
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.permissions import AllowAny
{%- endif %}


def health(request):
    return HttpResponse()

{% if cookiecutter.use_drf == "y" %}
schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version="v1",
    ),
    public=True,
    permission_classes=[AllowAny],
)
{%- endif %}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health, name="health"),
    {%- if cookiecutter.use_drf == "y" %}
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),
    {% endif %}
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


{% if cookiecutter.use_debug_toolbar == "y" -%}
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))
    ] + urlpatterns
{%- endif %}
