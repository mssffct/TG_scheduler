from factory import Faker
from factory.django import DjangoModelFactory, Password

from users.models import *

CORRECT_USERNAME = 'correct_user'
CORRECT_PASS = '12345678'


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User

    username = Faker('first_name')
    password = Password(CORRECT_PASS)
