from django.db import models


class Activity(models.Model):
    name = models.TextField()
    points = models.IntegerField()

    # Number of times this activity has been performed by a
    # single participant
    number_of_times = models.IntegerField(default=1, null=True)

    # Participant who performs this activity
    performer = models.ForeignKey('Participant',
                                  on_delete=models.CASCADE,
                                  null=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    number = models.IntegerField(primary_key=True)
    min_score = models.BigIntegerField()
    max_score = models.BigIntegerField()
    name = models.TextField()

    def __str__(self):
        return self.name


class BadgeActivity(models.Model):
    name = models.TextField()

    # Number of times a newcomer have to perform this activity
    # to get this badge.
    number_of_times = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.name


class Badge(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    details = models.TextField(null=True)

    # Activities a newcomer have to perform to get this badge
    b_activities = models.ManyToManyField(BadgeActivity)

    def __str__(self):
        return self.name


class Participant(models.Model):
    username = models.CharField(max_length=100, primary_key=True)

    # Total points earned by the participant
    score = models.IntegerField(default=0, null=True)

    # Current level
    level = models.ForeignKey(Level, on_delete=models.CASCADE,
                              default=1, null=True)

    # All the activities performed
    activities = models.ManyToManyField(Activity)

    # Badges earned by participant
    badges = models.ManyToManyField(Badge)

    def __str__(self):
        return self.username

    def add_points(self, points, activity_string):
        """
        Update score, level and add activities peformed.

        :param points: an integer value representing the
                       points earned by the participant
                       for performing an activity
        :param activity_string: represents the activity
                                performed by the participant
        """
        self.update_score_and_level(points)
        self.add_activity(points, activity_string)

    def deduct_points(self, points_to_deduct, activity_string):
        """
        Deduct points for performing some specific activities.
        """
        self.add_points(-points_to_deduct, activity_string)

    def find_level_for_score(self, score):
        """
        Find suitable level based on the total score earned.
        """
        level = Level.objects.get(min_score__lte=score, max_score__gt=score)
        return level

    def update_score_and_level(self, points):
        """
        Update score and level based on points.
        """
        if points < 0 and self.score < abs(points):
            new_score = self.score = 0
        else:
            self.score += points
            new_score = self.score

        new_level = self.find_level_for_score(new_score)
        if new_level.number > self.level.number:
            self.level = new_level

    def add_activity(self, points, activity_string):
        """
        Add activity to the participant.

        This method checks if the current activity is
        already peformed by the user, if yes, then it
        increase the 'number_of_times' field with one.
        If not then it adds a new activity to the participant.
        """
        if self.activities.filter(name=activity_string).exists():
            activity = Activity.objects.get(name=activity_string,
                                            performer=self.username)
            activity.number_of_times += 1
            activity.save()
        else:
            activity = Activity.objects.create(name=activity_string,
                                               points=points, performer=self)
            self.activities.add(activity)

    def find_badges_for_activity(self, activities):
        """
        Find the badge based on the activities peformed by the newcomer.

        :param activities: a QuerySet dict containing the 'name'
                           as key and 'name of the activity' as value
        :return: a badge object
        """
        activities = [activity['name'] for activity in activities]
        badge_objects_list = []
        badges = Badge.objects.all()
        for badge in badges:
            b_activities = badge.b_activities.values('name')
            b_activities = [b_activity['name'] for b_activity in b_activities]
            # Skip the badge which have no activities
            if len(b_activities) == 0:
                continue
            match_activity_list = []
            for b_activity in b_activities:
                # Check if this badge activity is peformed by the participant
                if b_activity in activities:
                    match_activity_list.append(1)
            if len(b_activities) == len(match_activity_list):
                # The participant have performed all the activities listed
                # in the badge
                badge_objects_list.append(badge)
        return badge_objects_list

    def add_badge(self, activities):
        """
        Add badge to newcomer based on the activities performed.
        """
        badges = self.find_badges_for_activity(activities)
        if len(badges) == 0:
            return
        for badge in badges:
            self.badges.add(badge)
