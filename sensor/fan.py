import RPi.GPIO as GPIO

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
    GPIO.cleanup()

