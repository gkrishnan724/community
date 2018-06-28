from data.newcomers import get_newcomers
from gamification.models import Participant


def create_newcomers():
    """
    Create newcomer which will be used in the gamification system.
    """
    newcomer_objects_list = []
    for newcomer in get_newcomers():
        newcomer_objects_list.append(
            Participant(username=newcomer))
    Participant.objects.bulk_create(newcomer_objects_list)
