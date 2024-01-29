from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers
from users.views import UserSettingsViewSet, UserViewSet, TokenCreate, TokenDestroy
from memos.views import MemosViewSet

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="TG Scheduler API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
# Memos
router.register(r'memos', MemosViewSet, basename='memos')
# Settings
router.register(r'settings', UserSettingsViewSet, basename='settings')
# Users
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('scheduler_admin/', admin.site.urls),
    path('api/auth/login/', TokenCreate.as_view()),
    path('api/auth/logout/', TokenDestroy.as_view()),
    path('api/', include(router.urls)),
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if not settings.DOCKER_CONTAINER_MODE:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
