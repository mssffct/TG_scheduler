from django.urls import path, include

from .views import *

urlpatterns = [
    path('memos/', UsersView.as_view()),
]