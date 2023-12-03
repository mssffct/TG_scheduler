from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save


class UserSettings(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='settings'
    )
    telegram_id = models.IntegerField(blank=True, null=True, verbose_name="Telegram ID")

    @classmethod
    def user_post_save(cls, sender, instance: User, created: bool, *args, **kwargs):
        if created:
            instance = cls(user=instance)
            instance.save()


post_save.connect(UserSettings.user_post_save, sender=User)
