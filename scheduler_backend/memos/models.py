from django.db import models
from django.contrib.auth.models import User


class Memo(models.Model):
    class MemoImportance(models.TextChoices):
        HIGH = 'high'
        MIDDLE = 'middle'
        LOW = 'low'

    class MemoStatus(models.TextChoices):
        SENT = 'sent'
        NOT_SENT = 'not_sent'

    creator = models.ForeignKey(User, verbose_name='creator', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=MemoStatus.choices, verbose_name='memo status', default=MemoStatus.NOT_SENT
    )
    importance = models.CharField(
        max_length=50, choices=MemoImportance.choices, verbose_name='memo importance level', null=True
    )
    theme = models.CharField(max_length=200, verbose_name='theme', null=True)
    description = models.CharField(max_length=500, verbose_name='description', null=True)
    time_to_send = models.DateTimeField(verbose_name='time to send')

    def __str__(self):
        return f'Memo {self.theme or ""}, Level {self.importance or "unknown"}, Creator {self.creator}'

    class Meta:
        verbose_name = 'Memo'
        verbose_name_plural = 'Memos'
