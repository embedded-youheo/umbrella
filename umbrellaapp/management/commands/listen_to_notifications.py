import select
import psycopg2
from django.core.management.base import BaseCommand
from django.db import connection
from django.core.cache import cache

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
            print('폴링시작')
            conn.poll()
            print(conn.notifies)
            while conn.notifies:
                notify = conn.notifies.pop(0)
                print(notify)
                self.stdout.write(self.style.SUCCESS(f"Received notification: {notify.payload}"))
                cache.set('sse_message', notify.payload)

                # 캐싱이 제대로 되었는지 확인
                cached_message = cache.get('sse_message')
                if cached_message:
                    self.stdout.write(self.style.SUCCESS(f"Cached message: {cached_message}"))
                else:
                    self.stdout.write(self.style.ERROR("Failed to cache the message"))
