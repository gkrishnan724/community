import logging

import requests

from data.models import (
    Issue,
    Label,
    )
from data.newcomers import get_newcomers
from data.models import Contributor
from data.web import web_url


def fetch_issues(hoster):
    """
    Get issues opened by newcomers

    :param hoster: a string representing hoster, e.g. 'github'
    :return: a json of issues data
    """
    logger = logging.getLogger(__name__)
    if hoster == 'github':
        IMPORT_URL = web_url + 'issues/github/all'
    elif hoster == 'gitlab':
        IMPORT_URL = web_url + 'issues/github/all'
    else:
        IMPORT_URL = 'https://pastebin.com/raw/VgYXYDEN'
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.get(
            url=IMPORT_URL,
            headers=headers,
        )
        response.raise_for_status()
    except Exception as e:
        logger.error(e)
        return
    issues = response.json()

    # Removing issues which are not opened by newcomers
    for issue in issues[:]:
        if issue['author'] not in get_newcomers():
            issues.remove(issue)
    return issues


def import_issue(hoster, issue):
    """
    Import issue data to database

    :param hoster: a string representing hoster
    :param issue: a dict containing issue's data
    """
    logger = logging.getLogger(__name__)
    number = issue.get('number')
    assignees = issue.pop('assignees')
    labels = issue.pop('labels')
    author = issue.pop('author')
    try:
        c = Contributor.objects.get(login=author)
        issue['author'] = c
        issue['hoster'] = hoster
        i, created = Issue.objects.get_or_create(
            **issue
            )

        # Saving assignees
        assignees_list = []
        for assignee in assignees:
            a = Contributor.objects.get(login=assignee)
            assignees_list.append(a)
        i.assignees.add(*assignees_list)

        # Saving labels
        labels_list = []
        for label in labels:
            l, created = Label.objects.get_or_create(name=label)
            labels_list.append(l)
        i.labels.add(*labels_list)
        logger.info('Issue, %s has been saved.' % c)
    except Exception as ex:
        logger.error(
            'Something went wrong saving this issue %s: %s'
            % (number, ex))
