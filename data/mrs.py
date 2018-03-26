import logging

import requests

from data.models import (
    MergeRequest,
    Label,
    IssueNumber,
    )
from data.newcomers import get_newcomers
from data.models import Contributor
from data.web import web_url


def fetch_mrs(hoster):
    """
    Get mrs opened by newcomers

    :param hoster: a string representing hoster, e.g. 'github'
    :return: a json of mrs data
    """
    logger = logging.getLogger(__name__)
    if hoster == 'github':
        IMPORT_URL = web_url + 'mrs/github/all'
    elif hoster == 'gitlab':
        IMPORT_URL = web_url + 'mrs/gitlab/all'
    else:
        IMPORT_URL = 'https://pastebin.com/raw/cTcbAh64'
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
    mrs = response.json()

    # Removing mrs which are not opened by newcomers
    for mr in mrs[:]:
        if mr['author'] not in get_newcomers():
            mrs.remove(mr)
    return mrs


def import_mr(hoster, mr):
    """
    Import mr data to database

    :param hoster: a string representing hoster
    :param mr: a dict containing mr's data
    """
    logger = logging.getLogger(__name__)
    number = mr.get('number')
    assignees = mr.pop('assignees')
    labels = mr.pop('labels')
    author = mr.pop('author')
    closes_issues = mr.pop('closes_issues')
    try:
        c = Contributor.objects.get(login=author)
        mr['author'] = c
        mr['hoster'] = hoster
        m, created = MergeRequest.objects.get_or_create(
            **mr
            )

        # Saving assignees
        assignees_list = []
        for assignee in assignees:
            a = Contributor.objects.get(login=assignee)
            assignees_list.append(a)
        m.assignees.add(*assignees_list)

        # Saving issues closes by this mr
        closes_issues_list = []
        for i_number in closes_issues:
            i = IssueNumber.objects.create(number=i_number)
            closes_issues_list.append(i)
        m.closes_issues.add(*closes_issues_list)

        # Saving labels on the mr
        labels_list = []
        for label in labels:
            l, created = Label.objects.get_or_create(name=label)
            labels_list.append(l)
        m.labels.add(*labels_list)
        logger.info('MR, %s has been saved.' % c)
    except Exception as ex:
        logger.error(
            'Something went wrong saving this mr %s: %s'
            % (number, ex))
