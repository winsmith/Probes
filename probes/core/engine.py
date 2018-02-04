import logging
from datetime import datetime, timedelta

from django.conf import settings

from probes.core.models import GameObject, Movable

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.INFO)
logger = logging.getLogger("Engine")


def advance_to_current():
    current_time = datetime.now()
    tick_zero_time = settings.TICK_ZERO
    elapsed_time: timedelta = current_time - tick_zero_time
    current_tick_number = elapsed_time / settings.TICK_TIMEDELTA
    logging.info(f"Current Tick Number: {current_tick_number}")

    objects_to_accelerate = Movable.objects.filter(tick_numer__lt=current_tick_number).order_by('tick_number')
    objects_to_advance = GameObject.objects.filter(tick_numer__lt=current_tick_number).order_by('tick_number')

    while objects_to_advance.count() > 0:
        logging.info(f"Accelerating {objects_to_accelerate.count()} movables...")
        for movable in objects_to_accelerate:
            for other_movable in objects_to_accelerate:
                # TODO: Barnes-Huttify this
                if other_movable == movable:
                    continue
                movable.accelerate(other_movable)
            movable.move()
            movable.save()

        logging.info(f"Ticking {objects_to_accelerate.count()} game objects...")
        for game_object in objects_to_advance:
            game_object.tick()
            game_object.save()

        objects_to_accelerate = Movable.objects.filter(tick_numer__lt=current_tick_number).order_by('tick_number')
        objects_to_advance = GameObject.objects.filter(tick_numer__lt=current_tick_number).order_by('tick_number')

