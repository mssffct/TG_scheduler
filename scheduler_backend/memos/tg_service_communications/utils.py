import os
import requests


class TGServiceError(Exception):
    pass


def send_tg_message(data: dict):
    try:
        url = f"{os.getenv('TG_HOST')}:{os.getenv('TG_PORT')}/{os.getenv('TG_SLUG')}/send_message"
        requests.post(url, json=data)
    except Exception:
        raise TGServiceError('Failed to send message')
