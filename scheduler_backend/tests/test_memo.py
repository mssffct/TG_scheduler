from django.test import TestCase, Client

from tests.factories import UserFactory, NotSentMemoFactory, SentMemoFactory


class MemoTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.sent_memo = SentMemoFactory()
        self.not_sent_memo = NotSentMemoFactory()
        response = self.client.post(
            '/api/auth/user/register/',
            {'username': 'user1', 'password': '12345678', 'password2': '12345678'}
        )

    def test_create_memo(self):
        """Tests that user receives list of his memos"""
        pass