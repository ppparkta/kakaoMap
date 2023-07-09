from django.db import models

class Marker(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    message = models.CharField(max_length=255)