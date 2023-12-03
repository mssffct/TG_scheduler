from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    tg_settings_presence = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'tg_settings_presence')

    def get_tg_settings_presence(self, instance):
        # For frontend to display notification
        return 1 if instance.settings.telegram_id else 0
