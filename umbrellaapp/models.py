from django.db import models

# 초음파 센서 데이터 저장 테이블
class UltrasonicData(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"UltrasonicData {self.id} at {self.timestamp}"

# 온습도 센서 데이터 저장 테이블
class TemperatureHumidityData(models.Model):
    id = models.AutoField(primary_key=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Temperature: {self.temperature}, Humidity: {self.humidity} at {self.timestamp}"

# 이벤트 로그 테이블
class EventLog(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_type = models.CharField(max_length=20)
    log_message = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"EventLog {self.id}: {self.sensor_type} - {self.log_message} at {self.timestamp}"

# 알림 테이블
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    read = models.BooleanField()

    def __str__(self):
        return f"Notification {self.id}: {self.notification} at {self.timestamp} (Read: {self.read})"

# 시스템 설정 테이블
class SystemSettings(models.Model):
    id = models.AutoField(primary_key=True)
    humidity_threshold = models.FloatField()
    notification_method = models.CharField(max_length=20)
    fan_duration = models.IntegerField()
    alarm = models.BooleanField()

    def __str__(self):
        return (f"SystemSettings {self.id}: Humidity Threshold {self.humidity_threshold}, "
                f"Notification Method {self.notification_method}, Fan Duration {self.fan_duration} seconds, "
                f"Alarm {'On' if self.alarm else 'Off'}")