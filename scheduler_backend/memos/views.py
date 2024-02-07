from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import MemosSerializer
from .models import Memo
from .docs_schema import memo_schema
from backend.responses import *
from backend.docs_schema import *


class MemosViewSet(ModelViewSet):
    serializer_class = MemosSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self) -> QuerySet:
        if getattr(self, "swagger_fake_view", False):
            return Memo.objects.none()
        return Memo.objects.filter(creator=self.request.app_user).all()

    @swagger_auto_schema(request_body=memo_schema, responses={
        200: openapi.Response("Success Memo create", schema=get_success_response('Saved successfully')),
        503: openapi.Response("Failed to create Memo", schema=get_error_response('Failed to save memo'))
    })
    def create(self, request: Request, *args, **kwargs) -> SuccessResponse | ErrorResponse:
        """Create Memo"""
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

    @swagger_auto_schema(responses={
        200: openapi.Response("Success Memo retrieve", schema=MemosSerializer),
        503: openapi.Response("Failed to retrieve Memo", schema=success_response)
    })
    def retrieve(self, request, *args, **kwargs):
        """Retrieve exact Memo"""
        try:
            memo = Memo.objects.filter(creator=self.request.app_user).get(id__exact=kwargs)
            data = self.serializer_class(memo).data
            return SuccessResponse(data)
        except ObjectDoesNotExist:
            return ErrorResponse(description='Failed to retrieve Memo')


    @swagger_auto_schema(responses={
        200: openapi.Response("Success memo delete", schema=success_response),
        503: openapi.Response("Failed to delete memo", schema=success_response)
    })
    def destroy(self, request: Request, *args, **kwargs) -> SuccessResponse | ErrorResponse:
        """Delete Memo"""
        try:
            with transaction.atomic():
                Memo.objects.get(id=kwargs.get('pk')).delete()
                return SuccessResponse('Deleted successfully')
        except Exception as ex:
            print(ex)
            return ErrorResponse(description='Failed to delete memo')

    @swagger_auto_schema(request_body=memo_schema, responses={
        200: openapi.Response("Success memo update", schema=success_response),
        503: openapi.Response("Failed to update memo", schema=success_response)
    })
    def partial_update(self, request: Request, *args, **kwargs) -> SuccessResponse | ErrorResponse:
        """Partial update Memo"""
        data = request.data
        try:
            with transaction.atomic():
                Memo.objects.filter(id=kwargs.get('pk')).update(**data)
                return SuccessResponse('Updated successfully')
        except Exception:
            return ErrorResponse(description='Failed to update memo')
