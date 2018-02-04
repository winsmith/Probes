from django.core.management.base import BaseCommand

from core.engine import advance_to_current


class Command(BaseCommand):
    help = 'Accelerates and updates all Game Objects to current time'

    def handle(self, *args, **options):
        self.stdout.write("Beginning universe update...")
        advance_to_current()
        self.stdout.write(self.style.SUCCESS('Done updating universe.'))
