"""
WSGI config for umbrella project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import threading

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'umbrella.settings')

application = get_wsgi_application()

def start_listen_to_notifications():
    from django.core.management import call_command
    call_command('listen_to_notifications')

def start_humidity_sensor():
    from sensor.dht22 import observe_humidity
    observe_humidity()

def start_ultrasonic_sensor():
    from sensor.ultrasonic import observe_entry_exit
    observe_entry_exit()

notification_thread = threading.Thread(target=start_listen_to_notifications)
notification_thread.daemon = True
notification_thread.start()

sensor_thread = threading.Thread(target=start_humidity_sensor)
sensor_thread.daemon = True
sensor_thread.start()

ultrasonic_thread = threading.Thread(target=start_ultrasonic_sensor)
ultrasonic_thread.daemon = True
ultrasonic_thread.start()
