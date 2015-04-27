from django.contrib import admin
from .models import LightSensor, TemperatureSensor


class SensorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['value']}),
        ('Date information', {'fields': ['reading_date'], 'classes': ['collapse']}),
    ]
    list_display = ('value', 'reading_date')
    list_filter = ['reading_date']


admin.site.register(LightSensor, SensorAdmin)
admin.site.register(TemperatureSensor, SensorAdmin)

# Register your models here.
