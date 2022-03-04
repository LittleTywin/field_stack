from django.contrib import admin
from core.models import SampleModel, SensorStation, DataPoint

class ButtonSampleAdmin(admin.ModelAdmin):
    readonly_fields=["timestamp","value"]

admin.site.register(SampleModel)
admin.site.register(DataPoint)
admin.site.register(SensorStation)
