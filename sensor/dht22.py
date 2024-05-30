import sys
import os
import django
import time
import board
import adafruit_dht
from django.db import transaction
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Django 프로젝트 설정 파일을 불러오기
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "umbrella.settings")
django.setup()

# Django 모델을 불러오기
from umbrellaapp.models import TemperatureHumidityData

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D7)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

        # Check if humidity is above a certain threshold
        if humidity > 30:  # 예시로 습도가 60% 이상인 경우
            # 데이터베이스에 저장
            TemperatureHumidityData.objects.create(
                temperature=temperature_c,
                humidity=humidity,
                timestamp=time.strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간을 문자열로 포맷
            )
            transaction.commit()
            print("Data saved successfully")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)


# import time
# import board
# import adafruit_dht

# # Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D7)

# # you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# # This may be necessary on a Linux single board computer like the Raspberry Pi,
# # but it will not work in CircuitPython.
# # dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

# while True:
#     try:
#         # Print the values to the serial port
#         temperature_c = dhtDevice.temperature
#         temperature_f = temperature_c * (9 / 5) + 32
#         humidity = dhtDevice.humidity
#         print(
#             "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
#                 temperature_f, temperature_c, humidity
#             )
#         )

#     except RuntimeError as error:
#         # Errors happen fairly often, DHT's are hard to read, just keep going
#         print(error.args[0])
#         time.sleep(2.0)
#         continue
#     except Exception as error:
#         dhtDevice.exit()
#         raise error

#     time.sleep(2.0)
