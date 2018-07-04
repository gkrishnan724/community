from django.core.management.base import BaseCommand

from gamification.create import (
    create_levels,
    create_badge_activity,
    create_badges,
    add_activity_to_badge,
    )
from gamification.newcomers import create_newcomers


class Command(BaseCommand):
    help = 'Create gamification data'

    def handle(self, *args, **options):
        create_levels()
        create_newcomers()
        create_badge_activity()
        create_badges()
        add_activity_to_badge()
