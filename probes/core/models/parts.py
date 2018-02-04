from django.db import models
from django.db.models import CASCADE

from probes.core.models.game_object import Spacecraft


class SpacecraftPart(models.Model):
    spacecraft = models.ForeignKey(Spacecraft, related_name='parts', on_delete=CASCADE())
    name = models.CharField(default="Unnamed Spacecraft Part")
    mass = models.FloatField(default=100.0)
