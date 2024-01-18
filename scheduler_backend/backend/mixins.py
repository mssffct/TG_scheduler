from rest_framework.viewsets import ModelViewSet


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
