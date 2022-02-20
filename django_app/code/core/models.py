from django.db import models

class SampleModel(models.Model):
    attachment=models.FileField()
    
class ButtonSample(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.BooleanField()