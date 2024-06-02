import time
import RPi.GPIO as GPIO
import sys
import os
import django
from django.db import transaction

# Django 프로젝트 설정 파일을 불러오기
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "umbrella.settings")
django.setup()

# Django 모델을 불러오기
from umbrellaapp.models import UltrasonicData, EventLog
from umbrellaapp.constants import PASS_EVENT, ULTRA_SONIC_DISTANCE_THRESHOLD

sensor_type = "ULTRA_SONIC"
trigPin = 18  # gpio 26, pin 5 of J25
echoPin = 21   # gpio J16 - pin3, GPIO 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def get_distance():
    GPIO.output(trigPin, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00002)
    GPIO.output(trigPin, GPIO.LOW)

    while GPIO.input(echoPin) == GPIO.LOW:
        startTime = time.time()
    while GPIO.input(echoPin) == GPIO.HIGH:
        travelTime = time.time() - startTime
        if travelTime > 0.1:  # timeout
            return -1

    distance = travelTime * 17000
    return distance

try:
    while True:
        distance = get_distance()
        if distance != -1:
            print("Distance: {:.2f} cm".format(distance))
            # 이벤트 로그 테이블에 저장
            if distance <= ULTRA_SONIC_DISTANCE_THRESHOLD:
                EventLog.objects.create(
                    sensor_type=sensor_type,
                    log_message=PASS_EVENT,
                    timestamp=time.strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간을 문자열로 포맷
                )
                transaction.commit()
                print("Data saved successfully")
            # 초음파 센서 테이블에 저장
            UltrasonicData.objects.create(
                distance=distance,
                timestamp=time.strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간을 문자열로 포맷
            )
            transaction.commit()
            print("Data saved successfully")
        else:
            print("Measurement timeout")
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
except Exception as error:
    GPIO.cleanup()
    raise error