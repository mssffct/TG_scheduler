from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='settings'
    )
    telegram_id = models.IntegerField(blank=True, null=True, verbose_name="Telegram ID")

