from gamification.models import (
    Level,
    BadgeActivity,
    Badge,
    )


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


def create_badge_activity():
    b_activity__object_list = [
        BadgeActivity(
            name='Created a newcomer bug'),
        BadgeActivity(
            name='Created a difficulty low bug'),
        BadgeActivity(
            name='Created a difficulty medium bug'),
        BadgeActivity(
            name='Created a difficulty high bug'),
        BadgeActivity(
            name='Created a low importance newcomer issue'),
        BadgeActivity(
            name='Created a low importance, low difficulty issue'),
        BadgeActivity(
            name='Created a low importance, medium difficulty issue'),
        BadgeActivity(
            name='Created a low importance, high difficulty issue'),
        BadgeActivity(
            name='Created a medium importance newcomer issue'),
        BadgeActivity(
            name='Created a medium importance, low difficulty issue'),
        BadgeActivity(
            name='Created a medium importance, medium difficulty issue'),
        BadgeActivity(
            name='Created a medium importance, high difficulty issue'),
        BadgeActivity(
            name='Created a high importance newcomer issue'),
        BadgeActivity(
            name='Created a high importance, low difficulty issue'),
        BadgeActivity(
            name='Created a high importance, medium difficulty issue'),
        BadgeActivity(
            name='Created a high importance, high difficulty issue'),
        BadgeActivity(name='Created a critical importance newcomer issue'),
        BadgeActivity(
            name='Created a critical importance, low difficulty issue'),
        BadgeActivity(
            name='Created a critical importance, medium difficulty issue'),
        BadgeActivity(
            name='Created a critical importance, high difficulty issue'),
        BadgeActivity(
            name='Created a newcomer documentation issue'),
        BadgeActivity(
            name='Created a low difficulty documentation issue'),
        BadgeActivity(
            name='Created a medium difficulty documentation issue'),
        BadgeActivity(
            name='Created a newcomer feature issue'),
        BadgeActivity(
            name='Created a low difficulty feature issue'),
        BadgeActivity(
            name='Created a medium difficulty feature issue'),
        BadgeActivity(
            name='Created a high difficulty feature issue'),
        BadgeActivity(
            name='Created a linter bear proposal issue'),
        BadgeActivity(
            name='Created a generic bear proposal issue'),
        BadgeActivity(
            name='Created a native bear proposal issue'),
        BadgeActivity(
            name='Created a newcomer issue'),
        BadgeActivity(
            name='Created a low difficulty issue'),
        BadgeActivity(
            name='Created a medium difficulty issue'),
        BadgeActivity(
            name='Created a high difficulty issue'),
        BadgeActivity(
            name='Created a duplicate issue'),
        BadgeActivity(
            name='Created a invalid issue'),
        BadgeActivity(
            name='Solved a newcomer bug'),
        BadgeActivity(
            name='Solved a difficulty low bug'),
        BadgeActivity(
            name='Solved a difficulty medium bug'),
        BadgeActivity(
            name='Solved a difficulty high bug'),
        BadgeActivity(
            name='Solved a low importance newcomer issue'),
        BadgeActivity(
            name='Solved a low importance, low difficulty issue'),
        BadgeActivity(
            name='Solved a low importance, medium difficulty issue'),
        BadgeActivity(
            name='Solved a low importance, high difficulty issue'),
        BadgeActivity(
            name='Solved a medium importance newcomer issue'),
        BadgeActivity(
            name='Solved a medium importance, low difficulty issue'),
        BadgeActivity(
            name='Solved a medium importance, medium difficulty issue'),
        BadgeActivity(
            name='Solved a medium importance, high difficulty issue'),
        BadgeActivity(
            name='Solved a high importance newcomer issue'),
        BadgeActivity(
            name='Solved a high importance, low difficulty issue'),
        BadgeActivity(
            name='Solved a high importance, medium difficulty issue'),
        BadgeActivity(
            name='Solved a high importance, high difficulty issue'),
        BadgeActivity(
            name='Solved a critical importance newcomer issue'),
        BadgeActivity(
            name='Solved a critical importance, low difficulty issue'),
        BadgeActivity(
            name='Solved a critical importance, medium difficulty issue'),
        BadgeActivity(
            name='Solved a critical importance, high difficulty issue'),
        BadgeActivity(
            name='Solved a newcomer documentation issue'),
        BadgeActivity(
            name='Solved a low difficulty documentation issue'),
        BadgeActivity(
            name='Solved a medium difficulty documentation issue'),
        BadgeActivity(
            name='Solved a low difficulty feature issue'),
        BadgeActivity(
            name='Solved a medium difficulty feature issue'),
        BadgeActivity(
            name='Solved a difficulty feature issue'),
        BadgeActivity(
            name='Solved a linter bear proposal issue'),
        BadgeActivity(
            name='Solved a generic bear proposal issue'),
        BadgeActivity(
            name='Solved a native bear proposal issue'),
        BadgeActivity(
            name='Solved a newcomer issue'),
        BadgeActivity(
            name='Solved a low difficulty issue'),
        BadgeActivity(
            name='Solved a medium difficulty issue'),
        BadgeActivity(
            name='Solved a high difficulty issue'),
        BadgeActivity(
            name='Closed a merge_request without merge'),
    ]
    BadgeActivity.objects.bulk_create(b_activity__object_list)


def create_badges():
    badge_objects_list = [
        Badge(
            number=1,
            name='The Bug Finder',
            details='The one who find bugs in the existing codebase',
        ),
        Badge(
            number=2,
            name='The Bear Hunter',
            details='The one who create issues about new bears',
        ),
        Badge(
            number=3,
            name='The Bear Writer',
            details='The one who write new bears',
        ),
        Badge(
            number=4,
            name='The Bug Solver',
            details='The one who find bugs in the existing codebase',
        ),
        Badge(
            number=5,
            name='The Helper',
            details='The one who help other newcomers',
        ),
        Badge(
            number=6,
            name='The Reviewer',
            details='The one who review others pull requests',
        ),
        Badge(
            number=7,
            name='The Super Reviewer',
            details='The one who is the legend of reviewing',
        ),
        Badge(
            number=8,
            name='The All-Rounder',
            details='The one who can apply for the org developer role',
        ),
    ]
    Badge.objects.bulk_create(badge_objects_list)


def add_activity_to_badge():

    # Adding activities to the bug hunter badge
    bug_hunter_badge = Badge.objects.get(
        name='The Bug Finder')
    bug_hunter_activity1 = BadgeActivity.objects.get(
        name='Created a newcomer bug')
    bug_hunter_activity2 = BadgeActivity.objects.get(
        name='Created a difficulty low bug')
    bug_hunter_activities_list = [
        bug_hunter_activity1,
        bug_hunter_activity2,
    ]
    bug_hunter_badge.b_activities.add(*bug_hunter_activities_list)

    # Adding activities to the bear hunter badge
    bear_hunter_badge = Badge.objects.get(
        name='The Bear Hunter')
    bear_hunter_activity1 = BadgeActivity.objects.get(
        name='Created a native bear proposal issue'
        )
    bear_hunter_activity2 = BadgeActivity.objects.get(
        name='Created a generic bear proposal issue'
        )
    bear_hunter_activities_list = [
        bear_hunter_activity1,
        bear_hunter_activity2,
    ]
    bear_hunter_badge.b_activities.add(*bear_hunter_activities_list)

    # Adding activities to the bear writer badge
    bear_writer_badge = Badge.objects.get(
        name='The Bear Writer')
    bear_writer_activity1 = BadgeActivity.objects.get(
        name='Solved a native bear proposal issue')
    bear_writer_activity2 = BadgeActivity.objects.get(
        name='Solved a generic bear proposal issue')
    bear_writer_activity3 = BadgeActivity.objects.get(
        name='Solved a linter bear proposal issue')
    bear_writer_activities_lits = [
        bear_writer_activity1,
        bear_writer_activity2,
        bear_writer_activity3,
    ]
    bear_writer_badge.b_activities.add(*bear_writer_activities_lits)

    # Adding activities to the bug solver badge
    bug_solver_badge = Badge.objects.get(
        name='The Bug Solver')
    bug_solver_activity1 = BadgeActivity.objects.get(
        name='Solved a newcomer bug')
    bug_solver_activity2 = BadgeActivity.objects.get(
        name='Solved a difficulty low bug')
    bug_solver_activities_list = [
        bug_solver_activity1,
        bug_solver_activity2,
    ]
    bug_solver_badge.b_activities.add(*bug_solver_activities_list)

    # Adding activities to the all-rounder badge
    all_rounder_badge = Badge.objects.get(
        name='The All-Rounder')
    all_rounder_activity1 = BadgeActivity.objects.get(
        name='Solved a newcomer issue')
    all_rounder_activity2 = BadgeActivity.objects.get(
        name='Solved a low difficulty issue')
    all_rounder_activities_list = [
        all_rounder_activity1,
        all_rounder_activity2,
    ]
    all_rounder_badge.b_activities.add(
        *all_rounder_activities_list)
