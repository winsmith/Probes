import logging

from game_object import Body

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.INFO)


class ProbesEngine:
    def __init__(self, start_time: int = 0):
        self.game_objects = []
        self.current_tick_number = start_time
        self.logger = logging.getLogger(self.__class__.__name__.ljust(20))

    def tick(self):
        self.current_tick_number = self.current_tick_number + 1
        self.logger.info(f"================== Tick {self.current_tick_number} ==================")

        for game_object in self.game_objects:
            if isinstance(game_object, Body):
                game_object.update_vector()
                game_object.move(1)
            game_object.tick()

    def run(self):
        while True:
            try:
                self.tick()
            except KeyboardInterrupt:
                print("Bye")
                return
