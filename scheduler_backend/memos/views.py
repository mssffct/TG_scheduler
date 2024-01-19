from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from django.db import transaction
from rest_framework.decorators import action
from django.db.models import QuerySet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import MemosSerializer
from .models import Memo
from .docs_schema import memo_schema
from backend.responses import *
from backend.docs_schema import *
from backend.mixins import MixedPermissionModelViewSet
from backend.permissions import IsCreator


class MemosViewSet(MixedPermissionModelViewSet):

    serializer_class = MemosSerializer
    permission_classes_by_action = {
        ('create', 'partial_update', 'destroy'): [IsCreator, ],
    }

    def get_queryset(self) -> QuerySet:
        if getattr(self, "swagger_fake_view", False):
            return Memo.objects.none()
        return Memo.objects.filter(creator=self.request.app_user).all()

    @swagger_auto_schema(request_body=memo_schema, responses={
        200: openapi.Response("Success memo create", schema=success_response),
        503: openapi.Response("Failed to create memo", schema=success_response)
    })
    def create(self, request: Request, *args, **kwargs) -> SuccessResponse | ErrorResponse:
        data = request.data
        try:
            with transaction.atomic():
                memo = Memo(
                    creator=request.app_user, **data
                )
                memo.save()
                return SuccessResponse(data={'message': 'Saved successfully'})
        except Exception as ex:
            print(ex)
            return ErrorResponse(description='Failed to save memo')

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return ErrorResponse(status=405)


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
