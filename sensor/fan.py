import os
import RPi.GPIO as GPIO
from time import sleep

pin = 6
maxTmp = 10

def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.setwarnings(False)

def getCPUTemperature():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","").replace("'C\n",""))

def checkTemperature():
        CPU_temp = float(getCPUTemperature())
        if CPU_temp>maxTmp:
                GPIO.output(pin, True)
        else:
                GPIO.output(pin, False)

try:
        setup()
        while True:
                checkTemperature()
                sleep(5)
except KeyboardInterrupt:
        GPIO.cleanup()