from gamification.models import Level


def create_levels():
    """
    Create levels which will be used in the gamification system.
    """
    level_objects_list = [
        Level(number=1, min_score=0, max_score=5, name='newbie'),
        Level(number=2, min_score=5, max_score=10, name='beginner'),
        Level(number=3, min_score=10, max_score=15, name='learner'),
        Level(number=4, min_score=15, max_score=20, name='intermediate'),
        Level(number=5, min_score=20, max_score=25, name='cool'),
        Level(number=6, min_score=25, max_score=30, name='awesome'),
        Level(number=7, min_score=30, max_score=35, name='master'),
        Level(number=8, min_score=35, max_score=40, name='legend'),
        Level(number=9, min_score=40, max_score=45, name='expert'),
    ]
    Level.objects.bulk_create(level_objects_list)
