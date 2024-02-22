from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def login(client: TestCase.client_class, password: str, user: User) -> None:
    client.post(
        '/api/auth/token/login/',
        dict(username=user.username, password=password)
    )
    token = Token.objects.get(user__username=user.username)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
