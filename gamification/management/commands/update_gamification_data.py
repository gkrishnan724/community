from django.core.management.base import BaseCommand

from gamification.update import (
    get_mr_objects,
    update_participants_data,
    get_participant_objects,
    award_badges,
    )


class Command(BaseCommand):
    help = 'Update gamification data'

    def handle(self, *args, **options):
        for mr in get_mr_objects():
            if mr.labels.count() == 0:
                continue
            update_participants_data(mr)
        for participant in get_participant_objects():
            award_badges(participant)
