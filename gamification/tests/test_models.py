from django.test import TestCase

from gamification.models import (
    Activity,
    Level,
    BadgeActivity,
    Badge,
    Participant,
    )


class ActivityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all methods
        Activity.objects.create(name='Created a newcomer bug',
                                points=5)

    def test_field_label(self):
        activity = Activity.objects.get(id=1)
        name = activity._meta.get_field('name').verbose_name
        points = activity._meta.get_field('points').verbose_name
        number_of_times = activity._meta.get_field(
            'number_of_times').verbose_name
        self.assertEquals(name, 'name')
        self.assertEquals(points, 'points')
        self.assertEquals(number_of_times, 'number of times')

    def test_object_name_is_activity_name(self):
        activity = Activity.objects.get(id=1)
        expected_object_name = 'Created a newcomer bug'
        self.assertEquals(expected_object_name, str(activity))


class LevelModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all methods
        Level.objects.create(number=1,
                             min_score=0, max_score=5, name='newbie')

    def test_field_label(self):
        level = Level.objects.get(number=1)
        number = level._meta.get_field('number').verbose_name
        min_score = level._meta.get_field('min_score').verbose_name
        max_score = level._meta.get_field('max_score').verbose_name
        name = level._meta.get_field('name').verbose_name
        self.assertEquals(number, 'number')
        self.assertEquals(min_score, 'min score')
        self.assertEquals(max_score, 'max score')
        self.assertEquals(name, 'name')

    def test_object_name_is_lavel_name(self):
        level = Level.objects.get(number=1)
        expected_object_name = 'newbie'
        self.assertEquals(expected_object_name, str(level))


class BadgeActivityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all methods
        BadgeActivity.objects.create(name='Created a newcomer bug')

    def test_field_label(self):
        b_activity = BadgeActivity.objects.get(id=1)
        name = b_activity._meta.get_field('name').verbose_name
        number_of_times = b_activity._meta.get_field(
            'number_of_times').verbose_name
        self.assertEquals(name, 'name')
        self.assertEquals(number_of_times, 'number of times')

    def test_object_name_is_badge_activity_name(self):
        b_activity = BadgeActivity.objects.get(id=1)
        expected_object_name = 'Created a newcomer bug'
        self.assertEquals(expected_object_name, str(b_activity))


class BadgeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all methods
        BadgeActivity.objects.create(
            name='Created a newcomer bug')
        Badge.objects.create(
            number=1,
            name='The Bug Finder')

    def test_field_label(self):
        badge = Badge.objects.get(number=1)
        number = badge._meta.get_field('number').verbose_name
        name = badge._meta.get_field('name').verbose_name
        details = badge._meta.get_field('details').verbose_name
        b_activities = badge._meta.get_field(
            'b_activities').verbose_name
        self.assertEquals(number, 'number')
        self.assertEquals(name, 'name')
        self.assertEquals(details, 'details')
        self.assertEquals(b_activities, 'b activities')

    def test_object_name_is_badge_name(self):
        badge = Badge.objects.get(number=1)
        expected_object_name = 'The Bug Finder'
        self.assertEquals(expected_object_name, str(badge))

    def test_many_to_many_field(self):
        badge = Badge.objects.get(number=1)
        b_activity = BadgeActivity.objects.get(id=1)
        badge.b_activities.add(b_activity)
        self.assertEquals(badge.b_activities.get(pk=b_activity.pk),
                          b_activity)


class ParticipantModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all methods
        Level.objects.create(number=1,
                             min_score=0, max_score=5,
                             name='newbie')
        Level.objects.create(number=2,
                             min_score=5, max_score=10,
                             name='beginner')
        BadgeActivity.objects.create(
            name='Created a newcomer bug')
        Badge.objects.create(
            number=1,
            name='The Bug Finder')
        Activity.objects.create(name='Created a newcomer bug',
                                points=5)
        Participant.objects.create(username='sks444')
        Participant.objects.create(username='test')

    def test_field_label(self):
        participant = Participant.objects.get(username='sks444')
        username = participant._meta.get_field(
            'username').verbose_name
        score = participant._meta.get_field('score').verbose_name
        level = participant._meta.get_field('level').verbose_name
        activities = participant._meta.get_field(
            'activities').verbose_name
        badges = participant._meta.get_field(
            'badges').verbose_name
        self.assertEquals(username, 'username')
        self.assertEquals(score, 'score')
        self.assertEquals(level, 'level')
        self.assertEquals(activities, 'activities')
        self.assertEquals(badges, 'badges')

    def test_object_name_is_participant_username(self):
        participant = Participant.objects.get(username='sks444')
        expected_object_name = 'sks444'
        self.assertEquals(expected_object_name,
                          str(participant))

    def test_class_meta_ordering(self):
        participant1 = Participant.objects.get(username='sks444')
        participant1.score = 5
        participant1.save()
        participant2 = Participant.objects.get(username='test')
        participant2.score = 10
        participant2.save()
        participants = Participant.objects.all()
        self.assertEquals(participants[0].username, 'test')
        self.assertEquals(participants[1].username, 'sks444')

    def test_add_points_method(self):
        participant = Participant.objects.get(username='sks444')
        points = 5
        activity_string = 'Created a newcomer bug'
        participant.add_points(points, activity_string)
        participant.save()
        self.assertEquals(participant.score, 5)
        self.assertEquals(participant.level.name, 'beginner')
        self.assertEquals(participant.activities.count(), 1)

    def test_deduct_points_method(self):
        participant = Participant.objects.get(username='sks444')
        participant.score = 5
        participant.save()
        points = 5
        activity_string = 'Closed a mr without merge'
        participant.deduct_points(points, activity_string)
        participant.save()
        self.assertEquals(participant.score, 0)
        self.assertEquals(participant.level.name, 'newbie')
        self.assertEquals(participant.activities.count(), 1)

    def test_find_level_for_score_method(self):
        participant = Participant.objects.get(username='sks444')
        level = participant.find_level_for_score(5)
        self.assertEquals(level.name, 'beginner')

    def test_update_score_and_level_method(self):
        participant = Participant.objects.get(username='sks444')
        # Before update
        self.assertEquals(participant.score, 0)
        self.assertEquals(participant.level.name, 'newbie')

        # Update
        participant.update_score_and_level(5)

        # After update
        self.assertEquals(participant.score, 5)
        self.assertEquals(participant.level.name, 'beginner')

    def test_add_activity_method(self):
        participant = Participant.objects.get(username='sks444')

        # Befor applying add_activity
        self.assertEquals(participant.activities.count(), 0)

        # Apply add_activity
        points = 5
        activity = 'Created a newcomer bug'
        participant.add_activity(points, activity)

        # After applying add_activity
        self.assertEquals(participant.activities.count(), 1)

        # Performing the same activity again
        participant.add_activity(points, activity)

        # No new activity added
        self.assertEquals(participant.activities.count(), 1)

        # Number of times this activity has been performed
        # by the participant
        same_activity = participant.activities.get(
            name=activity,
            performer=participant.username)

        # 'number_of_times' of old activity increased by one
        self.assertEquals(same_activity.number_of_times, 2)

    def test_find_badges_for_activity_method(self):
        participant = Participant.objects.get(username='sks444')
        activity = Activity.objects.get(id=1)
        participant.activities.add(activity)
        b_activity = BadgeActivity.objects.get(id=1)
        badge = Badge.objects.get(number=1)
        badge.b_activities.add(b_activity)
        activities = participant.activities.values('name')
        badges = participant.find_badges_for_activity(activities)
        self.assertEquals(len(badges), 1)
        self.assertEquals(badges[0].name, 'The Bug Finder')

    def test_add_badge_method(self):
        participant = Participant.objects.get(username='sks444')
        activity = Activity.objects.get(id=1)
        participant.activities.add(activity)
        b_activity = BadgeActivity.objects.get(id=1)
        badge = Badge.objects.get(number=1)
        badge.b_activities.add(b_activity)

        # Before applying add_badge method
        self.assertEquals(participant.badges.count(), 0)

        # Applying add_badge method
        activities = participant.activities.values('name')
        participant.add_badge(activities)

        # After applying add_badge method
        self.assertEquals(participant.badges.count(), 1)
