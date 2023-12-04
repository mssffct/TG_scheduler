from rest_framework.serializers import ModelSerializer

from memos.models import Memo


class MemosSerializer(ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'
