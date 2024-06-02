# import os
# import RPi.GPIO as GPIO
# from time import sleep

# pin = 6
# maxTmp = 10
# def ~($$$):
# def setup():
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(pin, GPIO.OUT)
#         GPIO.setwarnings(False)

# def getCPUTemperature():
#         temp = os.popen("vcgencmd measure_temp").readline()
#         return (temp.replace("temp=","").replace("'C\n",""))

# def checkTemperature():
#         CPU_temp = float(getCPUTemperature())
#         if $$$:
#                 GPIO.output(pin, True)
#         else:
#                 GPIO.output(pin, False)

# try:
#         setup()
#         while True:
#                 checkTemperature()
#                 sleep(5)
# except KeyboardInterrupt:
#         GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep

pin = 6

def set_fan_state(state):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    
    if state:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)
    
    # GPIO 정리
    sleep(1)  # 선택 사항: 작은 지연 추가
    GPIO.cleanup()

