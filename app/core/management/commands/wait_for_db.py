import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django command to pause execution until database is available. """

    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for db...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Db unavailable. Waiting 1s...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Db available!'))
