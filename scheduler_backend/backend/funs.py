import os
import django


def init_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canary_backend.settings')
    django.setup()
