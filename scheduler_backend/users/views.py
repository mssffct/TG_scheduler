from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Response as oResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.request import Request

from .serializers import UserSerializer, UserSettingsSerializer
from .models import *
from .docs_schema import *
from backend.responses import *
from backend.docs_schema import *
from backend.mixins import SwaggerIgnoreBasicMethodsViewSet


class UserViewSet(SwaggerIgnoreBasicMethodsViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    @swagger_auto_schema(responses={
        200: oResponse('Success', schema=user_info_schema),
        503: oResponse('Error', schema=get_error_response('Unauthorized'))
    })
    @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,))
    def info(self, request: Request) -> ErrorResponse | SuccessResponse:
        user = request.user
        if not user.is_active:
            return ErrorResponse(status=403)
        data = self.serializer_class(user).data
        return SuccessResponse(data)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,))
    def register(self, request: Request) -> ErrorResponse | SuccessResponse:
        data = request.data
        username, pass1, pass2 = data.get('username'), data.get('password'), data.pop('password2')
        if User.objects.filter(username=username).exists():
            return ErrorResponse(description='Please, choose another username')
        if not pass1 == pass2:
            return ErrorResponse(description='The entered passwords do not match')
        try:
            with transaction.atomic():
                serializer = UserSerializer(data=data)
                if serializer.is_valid():
                    User.objects.create_user(**data)
                    return SuccessResponse()
                else:
                    print(serializer.errors)
                    return ErrorResponse(description=serializer.errors)
        except Exception as ex:
            return ErrorResponse(description='Failed to create user account')


class TokenCreate(ObtainAuthToken):
    def post(self, request, *args, **kwargs) -> ErrorResponse | SuccessResponse:
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            return ErrorResponse(description='Incorrect password or username')
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return SuccessResponse({'auth_token': token.key})


class TokenDestroy(ObtainAuthToken):
    def post(self, request, *args, **kwargs) -> ErrorResponse | SuccessResponse:
        Token.objects.get(user=request.app_user).delete()
        return SuccessResponse()


class UserSettingsViewSet(SwaggerIgnoreBasicMethodsViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSettingsSerializer

    @action(methods=['get'], detail=False)
    def telegram_id(self, request: Request) -> SuccessResponse:
        settings = UserSettings.objects.get(user=request.app_user)
        return SuccessResponse({'telegram_id': settings.telegram_id or None})

    @action(methods=['post'], detail=False)
    def save_settings(self, request: Request, *args, **kwargs) -> ErrorResponse | SuccessResponse:
        data = request.data
        username, telegram_id = data.get('username'), data.get('telegram_id')
        if request.app_user.username == username:
            pass
        elif User.objects.filter(username=username).exists():
            return ErrorResponse(description='Please, choose another username')
        else:
            User.objects.filter(username=request.app_user).update(username=username)
        if telegram_id:
            try:
                UserSettings.objects.filter(user=request.app_user).update(telegram_id=telegram_id)
            except ValueError:
                return ErrorResponse(description='Please enter the correct telegram id number')
        return SuccessResponse('Saved successfully')
