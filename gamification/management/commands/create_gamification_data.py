from django.core.management.base import BaseCommand

from gamification.create import create_levels
from gamification.newcomers import create_newcomers


class Command(BaseCommand):
    help = 'Create gamification data'

    def handle(self, *args, **options):
        create_levels()
        create_newcomers()
