from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from users.models import UserSettings
from tests.factories import UserFactory


class UserSettingsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = UserFactory()
        self.user2 = UserFactory(username='user2')
        self.correct_user = 'correct_user'
        self.correct_pass = '12345678'

    def test_settings_creation(self):
        """Test settings creation"""
        self.assertTrue(UserSettings.objects.filter(user=self.user1).exists())

    def test_register_duplicate_username_constraint(self):
        """Test that user can't create account with existing username"""
        response = self.client.post(
            '/api/auth/user/register/',
            {'username': 'user2', 'password': '12345678', 'password2': '12345678'}
        )
        self.assertEquals(response.status_code, 503)
        self.assertEquals(response.data['description'], 'Please, choose another username')

    def test_register_mismatched_passwords(self):
        """Test that mismatched password will return ErrorResponse"""
        response = self.client.post(
            '/api/auth/user/register/',
            {'username': 'user1', 'password': '87654321', 'password2': '12345678'}
        )
        self.assertEquals(response.status_code, 503)
        self.assertEquals(response.data['description'], 'The entered passwords do not match')

    def test_token_create_and_destroy(self):
        """Test that incorrect password or username will return ErrorResponse else SuccessResponse
        When logout request Token deletes"""
        register_response = self.client.post(
            '/api/auth/user/register/',
            {'username': self.correct_user, 'password': self.correct_pass, 'password2': self.correct_pass}
        )
        self.assertEquals(register_response.status_code, 200)
        login_response = self.client.post(
            '/api/auth/token/login/',
            {'username': self.correct_user, 'password': self.correct_pass + '*&1'}
        )
        self.assertEquals(login_response.status_code, 503)
        self.assertEquals(login_response.data['description'], 'Incorrect password or username')
        login_response = self.client.post(
            '/api/auth/token/login/',
            {'username': self.correct_user, 'password': self.correct_pass}
        )
        self.assertEquals(login_response.status_code, 200)
        # check if Token created
        user = User.objects.get(username=self.correct_user)
        self.assertTrue(Token.objects.filter(user=user).exists())
