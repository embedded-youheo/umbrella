from django.urls import path
from . import views

urlpatterns = [
    path('sse/', views.humid_event_sse, name='sse'),
    path('save_temperature_humidity_data/', views.save_temperature_humidity_data, name='save_temperature_humidity_data'),
    path('get_humidity/', views.get_humidity, name='get_humidity'),
    path('save_ultrasonic_data/', views.save_ultrasonic_data, name='save_ultrasonic_data'),
    path('control_buzzer/', views.control_buzzer, name='control_buzzer'),
    path('control_fan/', views.control_fan, name='control_fan'),
    path('system_settings/', views.system_settings, name='system_settings'),
    path('event_log/', views.event_log, name='event_log'),
    path('notifications/', views.notifications, name='notifications'),
]
