from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from django.db import transaction
from rest_framework.decorators import action
from django.db.models import QuerySet

from .serializers import MemosSerializer
from .models import Memo
from backend.responses import *


class MemosViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MemosSerializer

    def get_queryset(self) -> QuerySet:
        return Memo.objects.filter(creator=self.request.app_user).all()

    @action(methods=['post'], detail=False)
    def create_memo(self, request: Request) -> SuccessResponse | ErrorResponse:
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

    @action(methods=['delete'], detail=False)
    def delete_memo(self, request: Request) -> SuccessResponse | ErrorResponse:
        data = request.data
        try:
            with transaction.atomic():
                Memo.objects.get(id=data['id']).delete()
                return SuccessResponse('Deleted successfully')
        except Exception as ex:
            print(ex)
            return ErrorResponse(description='Failed to delete memo')

    @action(methods=['put'], detail=False)
    def update_memo(self, request: Request) -> SuccessResponse | ErrorResponse:
        data = request.data
        memo_id = data.pop('id')
        print(data)
        try:
            with transaction.atomic():
                Memo.objects.filter(id=memo_id).update(**data)
                return SuccessResponse('Updates successfully')
        except Exception as ex:
            print(ex)
            return ErrorResponse(description='Failed to update memo')
