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
            self.accelerate(game_object)
            game_object.tick()

    def accelerate(self, body):
        if not isinstance(body, Body):
            return

        other_bodies = [game_object for game_object in self.game_objects if isinstance(game_object, Body)]

        # TODO: Barnes-Huttify this
        for other_body in other_bodies:
            body.accelerate(other_body)

        body.move(1)

    def run(self):
        while True:
            try:
                self.tick()
            except KeyboardInterrupt:
                print("Bye")
                return
