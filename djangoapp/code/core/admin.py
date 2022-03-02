from django.contrib import admin
from core.models import SampleModel, ButtonSample, DataPoint

class ButtonSampleAdmin(admin.ModelAdmin):
    readonly_fields=["timestamp","value"]

admin.site.register(SampleModel)
admin.site.register(ButtonSample,ButtonSampleAdmin)
admin.site.register(DataPoint)