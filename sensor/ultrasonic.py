import time
import RPi.GPIO as GPIO

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
        else:
            print("Measurement timeout")
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()

# import RPi.GPIO as gpio
# import time
# import sys
# import warnings
# warnings.filterwarnings('ignore')
# LED = 19
# TRIGER = 18
# ECHO = 21

# gpio.setmode(gpio.BCM)
# gpio.setup(TRIGER, gpio.OUT)
# gpio.setup(ECHO,gpio.IN)
# gpio.setup(LED, gpio.OUT)
# startTime = time.time()

# try:
#     while True:
#         gpio.output(TRIGER,gpio.LOW)
#         time.sleep(0.1)
#         gpio.output(TRIGER,gpio.HIGH)
#         time.sleep(0.00002)
#         gpio.output(TRIGER,gpio.LOW)

#         while gpio.input(ECHO) == gpio.LOW:
#             startTime = time.time()

#         while gpio.input(ECHO) == gpio.HIGH:
#             endTime = time.time()

#         period = endTime - startTime
#         dist1 = round(period * 1000000 / 58, 2)
#         print(dist1)
#         dist2 = round(period * 17241, 2)
#         print(dist2)
#         try:
#             if dist2 <= 20:
#                 print('error124')
#                 gpio.output(LED, gpio.HIGH)
#                 time.sleep(1)
#                 gpio.output(LED, gpio.LOW)
#                 time.sleep(1)
#         except KeyboardInterrupt:
#             print("error")
#         print('Dist1', dist1, 'cm', ', Dist2', dist2, 'cm')
# except KeyboardInterrupt:
#     gpio.cleanup()
#     sys.exit()