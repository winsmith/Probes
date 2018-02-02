from datetime import datetime

from math import sqrt


class Position:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class Vector(Position):
    pass

class GameObject:
    def __init__(self, current_game_time: datetime = datetime.now()):
        self.game_time = current_game_time

    def tick(self):
        raise NotImplemented("Subclass GameObject and add Mix-Ins")


class BodyMixin:
    position: Position
    vector: Vector

    def update_vector(self):
        # TODO
        pass

    def move(self, elapsed_ticks):
        pass


class SpaceCraftMixin:
    crew = []
    parts = []
    resources = {}


class SpaceCraft(GameObject, BodyMixin, SpaceCraftMixin):
    def __init__(self, position: Position, vector: Vector, current_game_time: datetime = datetime.now()):
        super().__init__(current_game_time)

        self.position = position
        self.vector = vector
        self.parts = []
        self.resources = {}

    def tick(self):
        pass


class Resource:
    name: str


class Body(GameObject, BodyMixin):
    def __init__(self, position: Position, vector: Vector, mass: float, current_game_time: datetime = datetime(0, 0, 0)):
        super().__init__(current_game_time)
        self.vector = vector
        self.position = position
        ;self.mass = mass

    def orbital_velocity(self, position: Position) -> float:
        """Return the orbital velocity an orbiting body should have"""
        r2 = sqrt(position.x * position.y + position.y)
        # TODO: Make three-dimensional
        numerator = 6.67e-11 * 1e6 * self.mass
        return sqrt(numerator / r2)



