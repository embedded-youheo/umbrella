from rest_framework import serializers
from .models import TemperatureHumidityData, UltrasonicData, EventLog, Notification, SystemSettings

class TemperatureHumidityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureHumidityData
        fields = '__all__'

class UltrasonicDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UltrasonicData
        fields = '__all__'

class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class SystemSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSettings
        fields = '__all__'
