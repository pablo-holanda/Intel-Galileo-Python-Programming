from django.contrib import admin
from .models import LightSensor, TemperatureSensor

admin.site.register(LightSensor)
admin.site.register(TemperatureSensor)

# Register your models here.
