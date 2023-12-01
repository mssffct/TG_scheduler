from django.urls import path, include

from .views import *

urlpatterns = [
    path('memos/', MemosView.as_view()),
]