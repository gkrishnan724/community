from functools import lru_cache

from data.models import Contributor
from community.git import get_org_name


@lru_cache(maxsize=32)
def get_newcomers():
    """
    Get newcomers list

    :return: the list of newcomer usernames
    """
    newcomers_list = []
    contributors = Contributor.objects.all()
    for contributor in contributors:
        # Get newcomers who belongs to only one team
        # and that is newcomers team.
        if contributor.teams.all().count() == 1:
            team = get_org_name() + ' newcomers'
            if contributor.teams.all()[0].name == team:
                newcomers_list.append(contributor.login)
    return newcomers_list
