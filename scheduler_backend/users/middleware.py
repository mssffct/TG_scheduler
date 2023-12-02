from typing import Union
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.authtoken.models import Token


# Add user to request
class TokenAuthMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        request.app_user = self.get_user_by_headers(request.headers)
        response = self._get_response(request)
        return response

    def get_user_by_headers(self, header: dict) -> Union[User, AnonymousUser]:
        authorisation: str = header.get('Authorization', '')
        if not authorisation.startswith('Token'):
            return get_user_model()

        token_string = authorisation.split(' ')[-1]
        user = Token.objects.select_related('user').get(key=token_string).user
        return user
