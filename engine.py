from datetime import datetime, timedelta

from game_object import GameObject


class ProbesEngine:
    def __init__(self, start_time: datetime = datetime(0, 0, 0)):
        self.game_objects = [GameObject]
        self.current_time = start_time

    def tick(self):
        self.current_time = self.current_time + timedelta(days=1)
        for game_object in self.game_objects:
            game_object.tick()
