from django.db import models
from django.db.models import CASCADE


class Resource(models.Model):
    name = models.CharField(max_length=255, default="Unnamed Resource")
    mass = models.FloatField(default=1.0)


class SpacecraftResource(models.Model):
    spacecraft = models.ForeignKey('Spacecraft', on_delete=CASCADE)
    resource = models.ForeignKey('Resource', on_delete=CASCADE)
    amount = models.FloatField(default=0.0)