from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TemperatureHumidityData, UltrasonicData, EventLog, Notification, SystemSettings
from .serializers import TemperatureHumidityDataSerializer, UltrasonicDataSerializer, EventLogSerializer, NotificationSerializer, SystemSettingsSerializer
from sensor.fan import control_fan

# 온습도 데이터 저장
@api_view(['POST'])
def save_temperature_humidity_data(request):
    if request.method == 'POST':
        serializer = TemperatureHumidityDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 실시간 습도 확인
@api_view(['GET'])
def get_humidity(request):
    if request.method == 'GET':
        latest_data = TemperatureHumidityData.objects.latest('timestamp')
        return Response({'humidity': latest_data.humidity}, status=status.HTTP_200_OK)

# 초음파 센서 데이터 저장
@api_view(['POST'])
def save_ultrasonic_data(request):
    if request.method == 'POST':
        serializer = UltrasonicDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 부저 제어 (단순히 상태를 반환하는 예제)
@api_view(['POST'])
def control_buzzer(request):
    # 특정 조건 처리 로직을 여기에 추가
    return Response({'message': 'Buzzer controlled'}, status=status.HTTP_200_OK)

# 팬 제어 (단순히 상태를 반환하는 예제)
# @api_view(['POST'])
# def control_fan(request):
#     # request body 깜 => $$$(   불리언)
#     $$$ = equest body 깜 
#     ~($$$)
#     # 특정 조건 처리 로직을 여기에 추가
#     return Response({'message': 'Fan controlled'}, status=status.HTTP_200_OK)
@api_view(['POST'])
def control_fan_view(request):
    try:
        data = json.loads(request.body)
        fan_state = data.get('state')
        
        if fan_state is not None:
            control_fan(fan_state)
            return Response({'message': 'Fan controlled'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid state value'}, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)

# 시스템 설정 조회 및 업데이트
@api_view(['GET', 'POST'])
def system_settings(request):
    if request.method == 'GET':
        settings = SystemSettings.objects.first()
        serializer = SystemSettingsSerializer(settings)
        return Response(serializer.data)
    elif request.method == 'POST':
        settings = SystemSettings.objects.first()
        serializer = SystemSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 이벤트 로그 조회
@api_view(['GET'])
def event_log(request):
    if request.method == 'GET':
        logs = EventLog.objects.all()
        serializer = EventLogSerializer(logs, many=True)
        return Response(serializer.data)

# 시스템 알림 조회
@api_view(['GET'])
def notifications(request):
    if request.method == 'GET':
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
