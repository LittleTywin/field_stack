from django.db import models

class SampleModel(models.Model):
    attachment=models.FileField()

class SensorStation(models.Model):
    id = models.IntegerField(primary_key=True)
class DataPoint(models.Model):
    timestamp = models.DateTimeField()
    tamper = models.BooleanField()
    tamperco = models.IntegerField()
    burner = models.BooleanField()
    burnerco = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    sensorstation = models.ForeignKey(SensorStation, on_delete=models.CASCADE)

    def populate(self,data):
        self.timestamp = data['timestamp']
        self.burner = data['burner']
        self.burnerco = data['burnerco']
        self.temperature = data['temperature']
        self.tamper = data['tamper']
        self.tamperco = data['tamperco']
        self.humidity = data['humidity']
        self.sensorstation = SensorStation.objects.get(id=data['stationid'])