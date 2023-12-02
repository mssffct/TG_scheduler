from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class UsersView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

