import os

from django_celery_beat.models import PeriodicTask, IntervalSchedule
from dotenv import load_dotenv


load_dotenv()


class MemosSendWorker:
    INTERVAL = os.getenv('TASK_INTERVAL')
    TASK = 'memos.tasks.send_task.send'
    NAME = 'MemosSendWorker'
    TIMEZONE = 'Europe/Moscow'

    @classmethod
    def initial(cls):
        try:
            cls._update_task()
        except Exception as ex:
            raise ex

    @classmethod
    def _update_task(cls):
        incident_interval, created = IntervalSchedule.objects.get_or_create(
            every=cls.INTERVAL,
            period=IntervalSchedule.SECONDS
        )
        incident_interval.save()

        task, created = PeriodicTask.objects.update_or_create(
            name=cls.NAME,
            defaults={
                'interval': incident_interval,
                'task': cls.TASK
            }
        )
