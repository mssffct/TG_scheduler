from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from .serializers import MemosSerializer
from .models import Memo


class MemosView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MemosSerializer

    def get_queryset(self, request: Request):
        return Memo.objects.filter(creator=request.app_user).all()

    def create(self, request: Request):
        pass
