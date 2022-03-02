from django.db import models

class SampleModel(models.Model):
    attachment=models.FileField()
    
class ButtonSample(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.BooleanField()

class DataPoint(models.Model):
    timestamp = models.DateTimeField()
    tamper = models.BooleanField()
    tamperCO = models.IntegerField()
    burner = models.BooleanField()
    burnerCO = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()