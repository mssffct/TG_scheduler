from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from .models import UserSettings
from memos.models import Memo


class UserSerializer(ModelSerializer):
    tg_settings_presence = serializers.SerializerMethodField()
    memos_statistics = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'tg_settings_presence', 'memos_statistics')

    def get_tg_settings_presence(self, instance):
        # For frontend to display notification
        return 1 if instance.settings.telegram_id else 0

    def get_memos_statistics(self, instance):
        memos = instance.memos or []
        data = {'overall': len(memos)}
        if memos:
            low, mid, high = 0, 0, 0
            for memo in memos:
                match memo.MemoImportance:
                    case memo.MemoImportance.LOW:
                        low += 1
                    case memo.MemoImportance.MIDDLE:
                        mid += 1
                    case memo.MemoImportance.HIGH:
                        high += 1
            data = data | {'low': low, 'mid': mid, 'high': high}
        return data




class UserSettingsSerializer(ModelSerializer):

    class Meta:
        model = UserSettings
        fields = '__all__'
