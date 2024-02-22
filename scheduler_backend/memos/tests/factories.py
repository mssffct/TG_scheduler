import random

from django.utils import timezone
from factory.django import DjangoModelFactory
from factory import Faker


from memos.models import *


class SentMemoFactory(DjangoModelFactory):
    theme = Faker('text')
    description = Faker('text')
    time_to_send = timezone.now()
    status = Memo.MemoStatus.SENT
    importance = random.choice(Memo.MemoImportance.choices)

    class Meta:
        model = Memo


class NotSentMemoFactory(DjangoModelFactory):
    theme = Faker('text')
    description = Faker('text')
    time_to_send = timezone.now()
    status = Memo.MemoStatus.NOT_SENT
    importance = random.choice(Memo.MemoImportance.choices)

    class Meta:
        model = Memo
