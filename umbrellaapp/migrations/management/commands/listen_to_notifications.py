import select
import psycopg2
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Listen to PostgreSQL notifications'

    def handle(self, *args, **kwargs):
        conn = connection.cursor().connection
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        curs = conn.cursor()
        curs.execute('LISTEN log_channel;')

        self.stdout.write(self.style.SUCCESS('Listening to log_channel...'))

        while True:
            if select.select([conn], [], [], 5) == ([], [], []):
                continue
            conn.poll()
            print(conn.notifies)
            while conn.notifies:
                notify = conn.notifies.pop(0)
                print(notify)
                self.stdout.write(self.style.SUCCESS(f"Received notification: {notify.payload}"))
                # SSE 수행