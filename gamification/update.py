import logging

from data.models import (
    MergeRequest,
    Issue,
    )
from gamification.activity import (
    get_issue_activity,
    get_merge_request_activity,
    )
from gamification.models import Participant


def get_mr_objects():
    """
    Get mrs objects saved in the database

    :return: a queryset of mr objects
    """
    mrs = MergeRequest.objects.all()
    return mrs


def update_participants_data(mr):
    """
    Update total score earned by the
    participant based on the activities performed,
    and the update the current level based on the
    total score.

    This method first check if the mr is merged or not,
    if it's merged, then get the activity and points based
    on the labels on mr and update the participant data who opened
    this mr.

    Further it gets all the issues this mr is closing and if its
    merged and then get the points and activity based on the labels
    on the issue and update the participant data who opened that issue.
    """
    logger = logging.getLogger(__name__)
    if mr.state == 'merged':
        labels = mr.labels.values('name')

        # Get the participant who opened this mr
        ncm = Participant.objects.get(username=mr.author)
        try:
            # Get activity and points based on labeles on the mr
            points, activity_string = get_merge_request_activity(labels)
        # Accept Exception if no activities found
        except Exception as ex:
            logger.error(ex)
            return
        # Update participant data
        ncm.add_points(points, activity_string)
        ncm.save()

        # Get all the issues numbers this mr is closing
        issues = mr.closes_issues.all()
        repo = mr.repo
        for issue in issues:
            # Get issue object from issue model
            i = Issue.objects.get(number=issue.number, repo=repo)
            i_labels = i.labels.values('name')

            # Get participant who opened the issue
            ncm = Participant.objects.get(username=i.author)

            # Get activity and points based on the labels on the issue
            points, activity_string = get_issue_activity(i_labels)

            # Update participant data who opened the issue
            ncm.add_points(points, activity_string)
            ncm.save()
    if mr.state == 'closed':
        ncm = Participant.objects.get(username=mr.author)
        points = 5
        activity = 'Closed a merge_request without merge'
        # Deduct 5 points for closing the merge_request
        ncm.deduct_points(points, activity)
        ncm.save()
