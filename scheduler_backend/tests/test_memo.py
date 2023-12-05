from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User

from tests.factories import UserFactory, NotSentMemoFactory, SentMemoFactory


class MemoTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserFactory(username='username1', password='12345678')
        self.user2 = UserFactory(username='user2')
        self.sent_memo = SentMemoFactory(creator=self.user)
        self.not_sent_memo = NotSentMemoFactory(creator=self.user2)

    def test_create_memo(self):
        """Tests that user receives list of his memos"""
        response = self.client.post(
            '/api/memos/create_memo/',
            {
                'theme': 'theme', 'description': 'description',
                'importance': 'low', 'time_to_send': timezone.now()
            }
        )
