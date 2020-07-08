import time

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # Django Command to pause execution until database is available
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database....')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
