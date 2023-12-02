from celery import shared_task
from django.utils import timezone
from django.db import transaction

from memos.models import Memo
from memos.tg_service_communications.utils import send_tg_message
from memos.tg_service_communications.templates import *


@shared_task
def send():
    """
    Task to send memos if they are not sent yet.
    Excludes memos with SENT status, sends messages to telegram_service sender microservice,
    finally bulk updates statuses of memos sent in this task iteration
    :return: None
    """
    # filter not sent yet
    now = timezone.now()
    memos = Memo.objects.filter(time_to_send__lte=now).exclude(status=Memo.MemoStatus.SENT).all()
    done: list = []
    for memo in memos:
        message = ''
        format_dict = dict(theme=memo.theme or "Without theme", description=memo.description or "Without description")
        match memo.importance:
            case Memo.MemoImportance.LOW:
                message = MEMO_MESSAGE_LOW.format(**format_dict)
            case Memo.MemoImportance.MIDDLE:
                message = MEMO_MESSAGE_MIDDLE.format(**format_dict)
            case Memo.MemoImportance.HIGH:
                message = MEMO_MESSAGE_MIDDLE.format(**format_dict)
        data = {
            "text": message, "chat_id": memo.creator.settings.telegram_id
        }
        send_tg_message(data)
        memo.status = Memo.MemoStatus.SENT
        done.append(memo)
    # set memo status to sent (bulk_update)
    Memo.objects.bulk_update(done, ['status'])
