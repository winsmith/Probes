from django.db import models
from django.db.models import CASCADE

from .game_object import Spacecraft


class SpacecraftPart(models.Model):
    spacecraft = models.ForeignKey(Spacecraft, related_name='parts', on_delete=CASCADE)
    name = models.CharField(max_length=255, default="Unnamed Spacecraft Part")
    mass = models.FloatField(default=100.0)
