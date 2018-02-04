from django.db import models
from math import sqrt
from django.conf import settings
from functools import reduce

from .resources import SpacecraftResource


class GameObject(models.Model):
    name = models.CharField(max_length=255, default="Unnamed GameObject")
    tick_number = models.IntegerField(default=0)

    def tick(self):
        self.tick_number += self.tick_number


class Positionable(GameObject):
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)
    z = models.FloatField(default=0.0)

    def distance_to(self, other_position: 'Positionable') -> float:
        """'
        Return the distance between two positions
        """
        dx = self.x - other_position.x
        dy = self.y - other_position.y
        dz = self.z - other_position.z
        return sqrt(dx * dx + dy * dy + dz * dz)


class Movable(Positionable):
    vx = models.FloatField(default=0.0)
    vy = models.FloatField(default=0.0)
    vz = models.FloatField(default=0.0)

    def get_mass(self) -> float:
        return 0.0

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def orbital_velocity(self, x, y, z) -> float:
        """Return the orbital velocity an orbiting body should have"""
        # TODO: Make three-dimensional
        r2 = sqrt(x * x + y * y)
        numerator = 6.67e-11 * 1e6 * self.get_mass()
        return sqrt(numerator / r2)

    def accelerate(self, other_movable: 'Movable'):
        """
        Compute the net force acting between this Movable and
        other_movable and add to the net force acting on this
        movable
        """
        if self == other_movable:
            return

        if other_movable is None:
            return

        # softening parameter (just to avoid infinities)
        eps = 3E4

        dx = self.x - other_movable.x
        dy = self.y - other_movable.y
        dz = self.z - other_movable.z
        dist = self.distance_to(other_movable)

        f = (settings.GRAVITATIONAL_CONSTANT * self.get_mass() * other_movable.get_mass()) / (dist * dist + eps * eps)
        self.vx += f * dx / dist
        self.vy += f * dy / dist
        self.vz += f * dz / dist


class Body(Movable):
    mass = models.FloatField(default=7.34767309e22)

    def get_mass(self):
        return self.mass


class Spacecraft(Movable):
    resources = models.ManyToManyField('Resource', through=SpacecraftResource)

    def get_mass(self):
        parts_mass = reduce(lambda x, y: x + y.mass, self.parts.all(), 0)
        # TODO: Resources Mass
        return parts_mass