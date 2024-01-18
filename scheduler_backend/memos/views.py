from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from django.db import transaction
from rest_framework.decorators import action
from django.db.models import QuerySet

from .serializers import MemosSerializer
from .models import Memo
from backend.responses import *
from backend.mixins import MixedPermissionModelViewSet
from backend.permissions import IsCreator


class MemosViewSet(MixedPermissionModelViewSet):
    serializer_class = MemosSerializer
    permission_classes_by_action = {
        ('list', 'create', 'partial_update', 'destroy'): [IsCreator, ]
    }

    def get_queryset(self) -> QuerySet:
        return Memo.objects.filter(creator=self.request.app_user).all()

    def create(self, request: Request, *args, **kwargs) -> SuccessResponse | ErrorResponse:
        data = request.data
        try:
            with transaction.atomic():
                memo = Memo(
                    creator=request.app_user, **data
                )
                memo.save()
                return SuccessResponse('Saved successfully')
        except Exception as ex:
            print(ex)
            return ErrorResponse(description='Failed to save memo')

    def retrieve(self, request, *args, **kwargs):
        #TODO Memo get function
        pass

    def destroy(self, request: Request, *args, **kwargs) -> SuccessResponse | ErrorResponse:
        data = request.data
        try:
            with transaction.atomic():
                Memo.objects.get(id=data['id']).delete()
                return SuccessResponse('Deleted successfully')
        except Exception as ex:
            print(ex)
            return ErrorResponse(description='Failed to delete memo')

    def partial_update(self, request: Request, *args, **kwargs) -> SuccessResponse | ErrorResponse:
        data = request.data
        memo_id = data.pop('id')
        try:
            with transaction.atomic():
                Memo.objects.filter(id=memo_id).update(**data)
                return SuccessResponse('Updated successfully')
        except Exception:
            return ErrorResponse(description='Failed to update memo')
