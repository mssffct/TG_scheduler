from django.db import transaction
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from django.contrib.auth.models import User

from .serializers import UserSerializer
from backend.responses import *


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,))
    def info(self, request: Request):
        user = request.user
        if not user.is_active:
            return ErrorResponse(status=403)
        data = self.serializer_class(user).data
        return SuccessResponse(data)

    @action(methods=['post'], detail=False)
    def check_password(self, request: Request, *args, **kwargs):
        user: User = request.user
        pwd = request.data['pwd']

        return SuccessResponse(user.check_password(pwd))

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,))
    def register(self, request: Request):
        data = request.data.dict()
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
                    return ErrorResponse(description=serializer.errors)
        except Exception as ex:
            return ErrorResponse(description='Failed to create user account')


class TokenCreate(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            return ErrorResponse(description='Incorrect password or username')
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return SuccessResponse({'auth_token': token.key})


class TokenDestroy(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        Token.objects.get(user=request.app_user).delete()
        return SuccessResponse()


class UserSettingsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
