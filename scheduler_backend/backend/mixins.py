from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema

from .responses import ErrorResponse


class MixedPermissionModelViewSet(ModelViewSet):
    """Миксин для разделения прав доступа к разным эндпоинтам и действиям ViewSet
    Использование: в дочернем классе ViewSet определить
    permission_classes_by_action = {
        (Кортеж нужных действий): [Нужные permissions],
        (Кортеж нужных действий): [Нужные permissions]
    }
    Необходимо перечислить все действия иначе к ним будет применены базовые права доступа
    """
    permission_classes_by_action = {}

    def get_permissions(self):
        # return permission_classes depending on `action`
        for actions in self.permission_classes_by_action.keys():
            if self.action in actions:
                return [permission() for permission in self.permission_classes_by_action[actions]]
            else:
                pass
        # return IsAuthenticated by default
        return [permission() for permission in self.permission_classes]


class SwaggerIgnoreBasicMethodsViewSet(ModelViewSet):
    def get_queryset(self):
        pass

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return ErrorResponse(status_code=405)

    @swagger_auto_schema(auto_schema=None)
    def list(self, request, *args, **kwargs):
        return ErrorResponse(status_code=405)

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        return ErrorResponse(status_code=405)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return ErrorResponse(status_code=405)

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return ErrorResponse(status_code=405)

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return ErrorResponse(status_code=405)
