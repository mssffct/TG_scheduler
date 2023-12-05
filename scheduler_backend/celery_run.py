import time
from threading import Thread
from typing import Callable

from celery.app.control import Inspect
from celery.apps.beat import Beat
from celery.apps.worker import Worker

from backend.funs import init_django
init_django()

from backend import celery_app
from celery.bin import worker


class CeleryManager:
    worker: Worker
    beat: Beat
    worker_thread: Thread
    beat_thread: Thread
    thread_quit: bool = False

    worker_thread_name = 'worker_thread'
    beat_thread_name = 'beat_thread'
    loglevel_str = '--loglevel=INFO'

    def __init__(self):
        from memos.tasks import send_task

    def target_decorator(self, target: Callable):
        target()
        self.thread_quit = True

    def _beat_target(self):
        cmd = ['beat', self.loglevel_str]
        cmd_str = ' '.join(cmd)

        try:
            celery_app.start(cmd_str)
        except Exception as ex:
            print(str(ex))

    def start_beat(self):
        self.beat_thread = Thread(
            name=self.beat_thread_name, target=lambda: self.target_decorator(self._beat_target)
        )
        self.beat_thread.start()

    def _worker_target(self):
        cmd = ['worker', self.loglevel_str]
        cmd_str = ' '.join(cmd)

        try:
            celery_app.worker_main(cmd_str)
        except Exception as ex:
            print(ex)
            print('[Worker]: Process start failed')

    def start_worker(self):
        self.worker_thread = Thread(
            name=self.worker_thread_name, target=lambda: self.target_decorator(self._worker_target)
        )
        self.worker_thread.start()

    def run(self):
        self.start_worker()
        self.start_beat()

        while True:
            if self.thread_quit:
                break

            time.sleep(1)


if __name__ == '__main__':
    celery_manager = CeleryManager()

    try:
        celery_manager.run()
    except Exception as ex:
        print(f'Celery failed to start: {ex}')
