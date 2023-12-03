from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('token/login/', TokenCreate.as_view()),
    path('token/logout/', TokenDestroy.as_view()),
]