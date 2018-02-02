from datetime import datetime


class Position:
    x: float
    y: float
    z: float

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


class GameObject:
    def __init__(self, current_game_time: datetime = datetime.now()):
        self.game_time = current_game_time

    def tick(self):
        raise NotImplemented("Subclass GameObject and add Mix-Ins")


class BodyMixin:
    position: Position
    vector = None

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
    def __init__(self, position: Position, current_game_time: datetime = datetime.now()):
        super().__init__(current_game_time)

        self.position = position
        self.vector = None
        self.parts = []
        self.resources = {}

    def tick(self):
        pass


class Resource:
    name: str


