from math import sqrt
import logging

from functools import reduce

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.INFO)
G = 6.673e-11  # gravitational constant


class GameObject:
    def __init__(self, name="unnamed GameObject", tick_number: int = 0):
        self.name = name
        self.tick_number = tick_number
        self.logger = logging.getLogger(self.name.ljust(20))

    def tick(self):
        pass


class Position:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other_position: 'Position') -> float:
        """'
        Return the distance between two positions
        """
        dx = self.x - other_position.x
        dy = self.y - other_position.y
        dz = self.z - other_position.z
        return sqrt(dx * dx + dy * dy + dz * dz)


class Vector(Position):
    pass


class Body(GameObject):
    position: Position
    vector: Vector

    def __init__(self, position: Position, vector: Vector, name="unnamed Body", tick_number: int = 0):
        super().__init__(name, tick_number)
        self.position = position
        self.vector = vector

    def move(self, elapsed_ticks):
        self.position.x += elapsed_ticks * self.vector.x
        self.position.y += elapsed_ticks * self.vector.y
        self.position.z += elapsed_ticks * self.vector.z
        self.logger.info(f"Moved to x{self.position.x} y{self.position.y} z{self.position.z}")

    def get_mass(self) -> float:
        pass

    def orbital_velocity(self, position: Position) -> float:
        """Return the orbital velocity an orbiting body should have"""
        r2 = sqrt(position.x * position.x + position.y * position.y)
        # TODO: Make three-dimensional
        numerator = 6.67e-11 * 1e6 * self.get_mass()
        return sqrt(numerator / r2)

    def distance_to(self, other_body: 'Body') -> float:
        """'
        Return the distance between two bodies
        """
        return self.position.distance_to(other_body.position)

    def accelerate(self, other_body: 'Body'):
        """
        Compute the net force acting between this body and
        other_body and add to the net force acting on this
        body
        """

        # These two checks are not in the original source
        if self == other_body:
            return

        if other_body is None:
            return

        # softening parameter (just to avoid infinities)
        eps = 3E4

        dx = self.position.x - other_body.position.x
        dy = self.position.y - other_body.position.y
        dz = self.position.z - other_body.position.z
        dist = self.distance_to(other_body)

        F = (G * self.get_mass() * other_body.get_mass()) / (dist*dist + eps*eps)
        self.vector.x += F * dx / dist
        self.vector.y += F * dy / dist
        self.vector.z += F * dz / dist


class Planetoid(Body):
    mass: float = 7.34767309e22

    def __init__(self, position: Position, vector: Vector, mass: float, name="unnamed Planetoid", tick_number: int = 0):
        super().__init__(position, vector, name, tick_number)
        self.mass = mass

    def get_mass(self):
        return self.mass

    def tick(self):
        self.logger.info("Planetoid Tick!")


class Resource:
    name: str


class CrewMember:
    name: str


class SpaceCraftPart:
    name: str
    mass: float

    def __init__(self, name="unnamed SpaceCraftPart", mass=20):
        self.name = name
        self.mass = mass


class SpaceCraft(Body):
    parts: [SpaceCraftPart]
    crew: [CrewMember]
    resources: [Resource]

    def __init__(self, position: Position, vector: Vector, name="unnamed SpaceCraft", tick_number: int = 0):
        super().__init__(position, vector, name, tick_number)

        self.parts = []
        self.crew = []
        self.resources = {}

    def tick(self):
        self.logger.info("Spacecraft Tick!")

    def get_mass(self):
        base_mass = 1
        parts_mass = reduce(lambda x, y: x+y.mass, self.parts, 0)
        return base_mass + parts_mass


