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
    def __init__(self, tick_number: int = 0):
        self.tick_number = tick_number

    def tick(self):
        pass


class Body(GameObject):
    position: Position
    vector: Vector

    def __init__(self, position: Position, vector: Vector, tick_number: int = 0):
        super().__init__(tick_number)
        self.position = position
        self.vector = vector

    def update_vector(self):
        # TODO
        pass

    def move(self, elapsed_ticks):
        pass

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

    def __init__(self, position: Position, vector: Vector, mass: float, tick_number: int = 0):
        super().__init__(position, vector, tick_number)
        self.mass = mass

    def get_mass(self):
        return self.mass


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

    def __init__(self, position: Position, vector: Vector, tick_number: int = 0):
        super().__init__(position, vector, tick_number)

        self.parts = []
        self.crew = []
        self.resources = {}

    def tick(self):
        pass


