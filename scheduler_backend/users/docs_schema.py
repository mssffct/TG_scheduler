from drf_yasg.openapi import Schema
from drf_yasg.openapi import TYPE_OBJECT, TYPE_STRING, TYPE_INTEGER

memo_statistics = {
    'overall': Schema(type=TYPE_INTEGER, description='amount of memos'),
    'low': Schema(type=TYPE_INTEGER, description='low importance memos amount'),
    'mid': Schema(type=TYPE_INTEGER, description='mid importance memos amount'),
    'high': Schema(type=TYPE_INTEGER, description='high importance memos amount')
}

user_info_schema = Schema(type=TYPE_OBJECT, properties={
    'id': Schema(type=TYPE_INTEGER, description='user id'),
    'username': Schema(type=TYPE_STRING, description='username'),
    'tg_settings_presence': Schema(type=TYPE_INTEGER, description='1 if tg chat id in settings and 0 if is not'),
} | memo_statistics)
