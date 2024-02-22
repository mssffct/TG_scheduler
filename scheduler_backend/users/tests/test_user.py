from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status

from users.models import UserSettings
from .factories import UserFactory, CORRECT_PASS, CORRECT_USERNAME
from .utils import login


AUTH_ENDPOINT = '/api/auth'


class UserSettingsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user1 = UserFactory()
        self.user2 = UserFactory(username='user2')

    def test_settings_creation(self):
        """Test settings creation"""
        self.assertTrue(UserSettings.objects.filter(user=self.user1).exists())

    def test_register_duplicate_username_constraint(self):
        """Test that user can't create account with existing username"""
        data = {'username': self.user2.username, 'password': CORRECT_PASS, 'password2': CORRECT_PASS}
        response = self.client.post(f'{AUTH_ENDPOINT}/user/register/', data, format='json')
        self.assertEquals(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEquals(response.data['description'], 'Please, choose another username')

    def test_register_mismatched_passwords(self):
        """Test that mismatched password will return ErrorResponse"""
        data = {'username': self.user1.username, 'password': '87654321', 'password2': CORRECT_PASS}
        response = self.client.post(f'{AUTH_ENDPOINT}/user/register/', data, format='json')
        self.assertEquals(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEquals(response.data['description'], 'The entered passwords do not match')

    def test_token_create_and_destroy(self):
        """Test that incorrect password or username will return ErrorResponse else SuccessResponse
        When logout request Token deletes"""
        # Wrong password
        data = {'username': CORRECT_USERNAME, 'password': f'{CORRECT_PASS}*&1'}
        login_response = self.client.post('/api/auth/token/login/', data, format="json")
        self.assertEquals(login_response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)
        self.assertEquals(login_response.data['description'], 'Incorrect password or username')

        login(self.client, CORRECT_PASS, self.user1)
        # check if Token created
        user = User.objects.get(username=self.user1)
        self.assertTrue(Token.objects.filter(user=user).exists())
