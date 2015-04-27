from django.db import models


class LightSensor(models.Model):
    value = models.IntegerField(default=0)
    reading_date = models.DateTimeField('date published')


class TemperatureSensor(models.Model):
    value = models.IntegerField(default=0)
    reading_date = models.DateTimeField('date published')

# Create your models here.
