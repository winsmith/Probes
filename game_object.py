from math import sqrt
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.INFO)


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


class Vector(Position):
    pass


class Body(GameObject):
    position: Position
    vector: Vector

    def __init__(self, position: Position, vector: Vector, name="unnamed Body", tick_number: int = 0):
        super().__init__(name, tick_number)
        self.position = position
        self.vector = vector

    def update_vector(self):
        # TODO
        pass

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


