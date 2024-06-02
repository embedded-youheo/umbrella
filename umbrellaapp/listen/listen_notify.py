import select
import psycopg2
from django.db import connection

def listen_to_channel():
    conn = connection.cursor().connection
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    curs = conn.cursor()
    curs.execute('LISTEN log_channel;')
    
    print('Listening to log_channel...')

    while True:
        if select.select([conn], [], [], 5) == ([], [], []):
            continue
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            print(f"Received notification: {notify.payload}")
            # 여기서 Django 채널 등을 통해 클라이언트에 SSE로 알림 전송
