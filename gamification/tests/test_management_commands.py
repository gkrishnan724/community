import unittest

from django.core.management import call_command
from django.test import TestCase

from gamification.models import (
    Level,
    Badge,
    Participant,
    BadgeActivity,
    )
from data.newcomers import get_newcomers


class CreateGamificationDataTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        call_command('create_gamification_data')

    def test_command_create_gamification_data(self):
        levels = Level.objects.all()
        if not levels:
            raise unittest.SkipTest(
                'There are no level')
        # There must be 9 levels created
        # as there are 9 levels listed in file create.py
        self.assertEquals(levels.count(), 9)

        b_activities = BadgeActivity.objects.all()
        # There must be 70 badge activities created
        # as there are 70 badge_activities listed in
        # file create.py
        self.assertEquals(b_activities.count(), 70)

        badges = Badge.objects.all()
        # There must be 8 badges created
        # as there are 8 badges listed in
        # file create.py
        self.assertEquals(badges.count(), 8)

        # The Bug Finder badge must have two activities
        badge1 = Badge.objects.get(name='The Bug Finder')
        self.assertEquals(badge1.b_activities.count(), 2)

        # The Bear Hunter badge must have two activities
        badge2 = Badge.objects.get(name='The Bear Hunter')
        self.assertEquals(badge2.b_activities.count(), 2)

        # The Bear Writer badge must have three activities
        badge3 = Badge.objects.get(name='The Bear Writer')
        self.assertEquals(badge3.b_activities.count(), 3)

        # The Bug Solver badge must have two activities
        badge4 = Badge.objects.get(name='The Bug Solver')
        self.assertEquals(badge4.b_activities.count(), 2)

        # The All-Rounder badge must have two activities
        badge5 = Badge.objects.get(name='The All-Rounder')
        self.assertEquals(badge5.b_activities.count(), 2)

        # Test created participant for the gamification app
        participants = Participant.objects.all()
        self.assertEquals(participants.count(), len(get_newcomers()))
