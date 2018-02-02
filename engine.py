from datetime import datetime, timedelta

from game_object import GameObject


class ProbesEngine:
    def __init__(self, start_time: int = 0):
        self.game_objects = []
        self.current_tick_number = start_time

    def tick(self):
        self.current_tick_number = self.current_tick_number + 1
        for game_object in self.game_objects:
            game_object.tick()

    def run(self):
        while True:
            try:
                self.tick()
            except KeyboardInterrupt:
                print("Bye")
                return
