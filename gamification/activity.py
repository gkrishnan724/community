from gamification.points import (

    NEWCOMER_DIFFICULTY_BUG_ISSUE,
    NEWCOMER_DIFFICULTY_LOW_IMPORTANCE_ISSUE,
    NEWCOMER_DIFFICULTY_MEDIUM_IMPORTANCE_ISSUE,
    NEWCOMER_DIFFICULTY_HIGH_IMPORTANCE_ISSUE,
    NEWCOMER_DIFFICULTY_CRITICAL_IMPORTANCE_ISSUE,
    NEWCOMER_DIFFICULTY_DOCUMENTATION_ISSUE,
    NEWCOMER_DIFFICULTY_FEATURE_ISSUE,
    LOW_DIFFICULTY_BUG_ISSUE,
    LOW_DIFFICULTY_LOW_IMPORTANCE_ISSUE,
    LOW_DIFFICULTY_MEDIUM_IMPORTANCE_ISSUE,
    LOW_DIFFICULTY_HIGH_IMPORTANCE_ISSUE,
    LOW_DIFFICULTY_FEATURE_ISSUE,
    LOW_DIFFICULTY_CRITICAL_IMPORTANCE_ISSUE,
    LOW_DIFFICULTY_DOCUMENTATION_ISSUE,
    MEDIUM_DIFFICULTY_LOW_IMPORTANCE_ISSUE,
    MEDIUM_DIFFICULTY_MEDIUM_IMPORTANCE_ISSUE,
    MEDIUM_DIFFICULTY_HIGH_IMPORTANCE_ISSUE,
    MEDIUM_DIFFICULTY_CRITICAL_IMPORTANCE_ISSUE,
    MEDIUM_DIFFICULTY_DOCUMENTATION_ISSUE,
    MEDIUM_DIFFICULTY_FEATURE_ISSUE,
    MEDIUM_DIFFICULTY_BUG_ISSUE,
    HIGH_DIFFICULTY_BUG_ISSUE,
    HIGH_DIFFICULTY_LOW_IMPORTANCE_ISSUE,
    HIGH_DIFFICULTY_MEDIUM_IMPORTANCE_ISSUE,
    HIGH_DIFFICULTY_HIGH_IMPORTANCE_ISSUE,
    HIGH_DIFFICULTY_CRITICAL_IMPORTANCE_ISSUE,
    HIGH_DIFFICULTY_FEATURE_ISSUE,
    NATIVE_BEAR_ISSUE,
    LINTER_BEAR_ISSUE,
    GENERIC_BEAR_ISSUE,
    DUPLICATE_ISSUE,
    INVALID_ISSUE,

    NEWCOMER_DIFFICULTY_BUG_MR,
    NEWCOMER_DIFFICULTY_LOW_IMPORTANCE_MR,
    NEWCOMER_DIFFICULTY_MEDIUM_IMPORTANCE_MR,
    NEWCOMER_DIFFICULTY_HIGH_IMPORTANCE_MR,
    NEWCOMER_DIFFICULTY_CRITICAL_IMPORTANCE_MR,
    NEWCOMER_DIFFICULTY_DOCUMENTATION_MR,
    NEWCOMER_DIFFICULTY_FEATURE_MR,
    LOW_DIFFICULTY_FEATURE_MR,
    LOW_DIFFICULTY_BUG_MR,
    LOW_DIFFICULTY_LOW_IMPORTANCE_MR,
    LOW_DIFFICULTY_MEDIUM_IMPORTANCE_MR,
    LOW_DIFFICULTY_HIGH_IMPORTANCE_MR,
    LOW_DIFFICULTY_DOCUMENTATION_MR,
    LOW_DIFFICULTY_CRITICAL_IMPORTANCE_MR,
    MEDIUM_DIFFICULTY_BUG_MR,
    MEDIUM_DIFFICULTY_LOW_IMPORTANCE_MR,
    MEDIUM_DIFFICULTY_MEDIUM_IMPORTANCE_MR,
    MEDIUM_DIFFICULTY_HIGH_IMPORTANCE_MR,
    MEDIUM_DIFFICULTY_DOCUMENTATION_MR,
    MEDIUM_DIFFICULTY_FEATURE_MR,
    MEDIUM_DIFFICULTY_CRITICAL_IMPORTANCE_MR,
    HIGH_DIFFICULTY_LOW_IMPORTANCE_MR,
    HIGH_DIFFICULTY_MEDIUM_IMPORTANCE_MR,
    HIGH_DIFFICULTY_HIGH_IMPORTANCE_MR,
    HIGH_DIFFICULTY_CRITICAL_IMPORTANCE_MR,
    HIGH_DIFFICULTY_FEATURE_MR,
    HIGH_DIFFICULTY_BUG_MR,
    NATIVE_BEAR_MR,
    LINTER_BEAR_MR,
    GENERIC_BEAR_MR,
    )


def get_issue_activity(labels):
    """
    Get activity based on the labels on the issues.

    :param labels: a QuerySet dict containing the 'name'
                   as key and 'name of the label' as value
    :return: a touple of points and activity string
    """
    labels = [label['name'] for label in labels]
    if 'difficulty/newcomer' in labels:
        if 'type/bug' in labels:
            activity = 'Created a newcomer bug'
            points = NEWCOMER_DIFFICULTY_BUG_ISSUE
            return points, activity

        if 'importance/low' in labels:
            activity = 'Created a low importance newcomer issue'
            points = NEWCOMER_DIFFICULTY_LOW_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/medium' in labels:
            activity = 'Created a medium importance newcomer issue'
            points = NEWCOMER_DIFFICULTY_MEDIUM_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/high' in labels:
            activity = 'Created a high importance newcomer issue'
            points = NEWCOMER_DIFFICULTY_HIGH_IMPORTANCE_ISSUE
            return points, activity
        if 'importance/critical' in labels:
            activity = 'Created a critical importance newcomer issue'
            points = NEWCOMER_DIFFICULTY_CRITICAL_IMPORTANCE_ISSUE
            return points, activity

        if 'area/documentation' in labels:
            activity = 'Created a newcomer documentation issue'
            points = NEWCOMER_DIFFICULTY_DOCUMENTATION_ISSUE
            return points, activity

        if 'type/feature' in labels:
            activity = 'Created a newcomer feature issue'
            points = NEWCOMER_DIFFICULTY_FEATURE_ISSUE
            return points, activity

    if 'difficulty/low' in labels:
        if 'type/bug' in labels:
            activity = 'Created a difficulty low bug'
            points = LOW_DIFFICULTY_BUG_ISSUE
            return points, activity

        if 'importance/low' in labels:
            activity = 'Created a low importance, low difficulty issue'
            points = LOW_DIFFICULTY_LOW_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/medium' in labels:
            activity = 'Created a medium importance, low difficulty issue'
            points = LOW_DIFFICULTY_MEDIUM_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/high' in labels:
            activity = 'Created a high importance, low difficulty issue'
            points = LOW_DIFFICULTY_HIGH_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/critical' in labels:
            activity = 'Created a critical importance, low difficulty issue'
            points = LOW_DIFFICULTY_CRITICAL_IMPORTANCE_ISSUE
            return points, activity

        if 'area/documentation' in labels:
            activity = 'Created a low difficulty documentation issue'
            points = LOW_DIFFICULTY_DOCUMENTATION_ISSUE
            return points, activity

        if 'type/feature' in labels:
            activity = 'Created a low difficulty feature issue'
            points = LOW_DIFFICULTY_FEATURE_ISSUE
            return points, activity

    if 'difficulty/medium' in labels:
        if 'type/bug' in labels:
            activity = 'Created a difficulty medium bug'
            points = MEDIUM_DIFFICULTY_BUG_ISSUE
            return points, activity

        if 'importance/low' in labels:
            activity = 'Created a low importance, medium difficulty issue'
            points = MEDIUM_DIFFICULTY_LOW_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/medium' in labels:
            activity = 'Created a medium importance, medium difficulty issue'
            points = MEDIUM_DIFFICULTY_MEDIUM_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/high' in labels:
            activity = 'Created a high importance, medium difficulty issue'
            points = MEDIUM_DIFFICULTY_HIGH_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/critical' in labels:
            activity = 'Created a critical importance, medium difficulty issue'
            points = MEDIUM_DIFFICULTY_CRITICAL_IMPORTANCE_ISSUE
            return points, activity

        if 'area/documentation' in labels:
            activity = 'Created a medium difficulty documentation issue'
            points = MEDIUM_DIFFICULTY_DOCUMENTATION_ISSUE
            return points, activity

        if 'type/feature' in labels:
            activity = 'Created a medium difficulty feature issue'
            points = MEDIUM_DIFFICULTY_FEATURE_ISSUE
            return points, activity

    if 'difficulty/high' in labels:
        if 'type/bug' in labels:
            activity = 'Created a difficulty high bug'
            points = HIGH_DIFFICULTY_BUG_ISSUE
            return points, activity

        if 'importance/low' in labels:
            activity = 'Created a low importance, high difficulty issue'
            points = HIGH_DIFFICULTY_LOW_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/medium' in labels:
            activity = 'Created a medium importance, high difficulty issue'
            points = HIGH_DIFFICULTY_MEDIUM_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/high' in labels:
            activity = 'Created a high importance, high difficulty issue'
            points = HIGH_DIFFICULTY_HIGH_IMPORTANCE_ISSUE
            return points, activity

        if 'importance/critical' in labels:
            activity = 'Created a critical importance newcomer issue'
            points = HIGH_DIFFICULTY_CRITICAL_IMPORTANCE_ISSUE
            return points, activity

        if 'type/feature' in labels:
            activity = 'Created a high difficulty feature issue'
            points = HIGH_DIFFICULTY_FEATURE_ISSUE
            return points, activity

        if 'type/bug' in labels:
            activity = 'Created a high difficulty bug issue'
            points = HIGH_DIFFICULTY_BUG_ISSUE
            return points, activity

    if 'bear/proposal' in labels:
        if 'area/lintbears' in labels:
            activity = 'Created a linter bear proposal issue'
            points = LINTER_BEAR_ISSUE
            return points, activity

        if 'area/genericbears' in labels:
            activity = 'Created a generic bear proposal issue'
            points = GENERIC_BEAR_ISSUE
            return points, activity

        activity = 'Created a native bear proposal issue'
        points = NATIVE_BEAR_ISSUE
        return points, activity

    if 'status/duplicate' in labels:
        activity = 'Created a duplicate issue'
        points = DUPLICATE_ISSUE
        return points, activity

    if 'status/invalid' in labels:
        activity = 'Created a invalid issue'
        points = INVALID_ISSUE
        return points, activity


def get_merge_request_activity(labels):
    """
    Get activity based on the labels on the mrs.

    :param labels: a QuerySet dict containing the 'name'
                   as key and 'name of the label' as value
    :return: a touple of points and activity string
    """
    labels = [label['name'] for label in labels]
    if 'difficulty/newcomer' in labels:
        if 'type/bug' in labels:
            activity = 'Solved a newcomer bug'
            points = NEWCOMER_DIFFICULTY_BUG_MR
            return points, activity

        if 'importance/low' in labels:
            activity = 'Solved a low importance newcomer issue'
            points = NEWCOMER_DIFFICULTY_LOW_IMPORTANCE_MR
            return points, activity

        if 'importance/medium' in labels:
            activity = 'Solved a medium importance newcomer issue'
            points = NEWCOMER_DIFFICULTY_MEDIUM_IMPORTANCE_MR
            return points, activity

        if 'importance/high' in labels:
            activity = 'Solved a high importance newcomer issue'
            points = NEWCOMER_DIFFICULTY_HIGH_IMPORTANCE_MR
            return points, activity

        if 'importance/critical' in labels:
            activity = 'Solved a critical importance newcomer issue'
            points = NEWCOMER_DIFFICULTY_CRITICAL_IMPORTANCE_MR
            return points, activity

        if 'area/documentation' in labels:
            activity = 'Solved a newcomer documentation issue'
            points = NEWCOMER_DIFFICULTY_DOCUMENTATION_MR
            return points, activity

        if 'type/feature' in labels:
            activity = 'Solved a newcomer feature issue'
            points = NEWCOMER_DIFFICULTY_FEATURE_MR
            return points, activity

    if 'difficulty/low' in labels:
        if 'type/bug' in labels:
            activity = 'Solved a difficulty low bug'
            points = LOW_DIFFICULTY_BUG_MR
            return points, activity

        if 'importance/low' in labels:
            activity = 'Solved a low importance, low difficulty issue'
            points = LOW_DIFFICULTY_LOW_IMPORTANCE_MR
            return points, activity

        if 'importance/medium' in labels:
            activity = 'Solved a medium importance, low difficulty issue'
            points = LOW_DIFFICULTY_MEDIUM_IMPORTANCE_MR
            return points, activity

        if 'importance/high' in labels:
            activity = 'Solved a high importance, low difficulty issue'
            points = LOW_DIFFICULTY_HIGH_IMPORTANCE_MR
            return points, activity

        if 'importance/critical' in labels:
            activity = 'Solved a critical importance, low difficulty issue'
            points = LOW_DIFFICULTY_CRITICAL_IMPORTANCE_MR
            return points, activity

        if 'area/documentation' in labels:
            activity = 'Solved a low difficulty documentation issue'
            points = LOW_DIFFICULTY_DOCUMENTATION_MR
            return points, activity

        if 'type/feature' in labels:
            activity = 'Solved a low difficulty feature issue'
            points = LOW_DIFFICULTY_FEATURE_MR
            return points, activity

    if 'difficulty/medium' in labels:
        if 'type/bug' in labels:
            activity = 'Solved a difficulty medium bug'
            points = MEDIUM_DIFFICULTY_BUG_MR
            return points, activity

        if 'importance/low' in labels:
            activity = 'Solved a low importance, medium difficulty issue'
            points = MEDIUM_DIFFICULTY_LOW_IMPORTANCE_MR
            return points, activity

        if 'importance/medium' in labels:
            activity = 'Solved a medium importance, medium difficulty issue'
            points = MEDIUM_DIFFICULTY_MEDIUM_IMPORTANCE_MR
            return points, activity

        if 'importance/high' in labels:
            activity = 'Solved a high importance, medium difficulty issue'
            points = MEDIUM_DIFFICULTY_HIGH_IMPORTANCE_MR
            return points, activity

        if 'importance/critical' in labels:
            activity = 'Solved a critical importance, medium difficulty issue'
            points = MEDIUM_DIFFICULTY_CRITICAL_IMPORTANCE_MR
            return points, activity

        if 'area/documentation' in labels:
            activity = 'Solved a medium documentation issue'
            points = MEDIUM_DIFFICULTY_DOCUMENTATION_MR
            return points, activity

        if 'type/feature' in labels:
            activity = 'Solved a medium difficulty feature issue'
            points = MEDIUM_DIFFICULTY_FEATURE_MR
            return points, activity

    if 'difficulty/high' in labels:
        if 'type/bug' in labels:
            activity = 'Solved a difficulty high bug'
            points = HIGH_DIFFICULTY_BUG_MR
            return points, activity

        if 'importance/low' in labels:
            activity = 'Solved a low importance, high difficulty issue'
            points = HIGH_DIFFICULTY_LOW_IMPORTANCE_MR
            return points, activity

        if 'importance/medium' in labels:
            activity = 'Solved a medium importance, high difficulty issue'
            points = HIGH_DIFFICULTY_MEDIUM_IMPORTANCE_MR
            return points, activity

        if 'importance/high' in labels:
            activity = 'Solved a high importance, high difficulty issue'
            points = HIGH_DIFFICULTY_HIGH_IMPORTANCE_MR
            return points, activity

        if 'importance/critical' in labels:
            activity = 'Solved a critical importance, high difficulty issue'
            points = HIGH_DIFFICULTY_CRITICAL_IMPORTANCE_MR
            return points, activity

        if 'type/feature' in labels:
            activity = 'Solved a newcomer feature issue'
            points = HIGH_DIFFICULTY_FEATURE_MR
            return points, activity

    if 'bear/proposal' in labels:
        if 'area/lintbears' in labels:
            activity = 'Created a linter bear'
            points = LINTER_BEAR_MR
            return points, activity

        if 'area/genericbears' in labels:
            activity = 'Created a generic bear'
            points = GENERIC_BEAR_MR
            return points, activity

        activity = 'Created a native bear'
        points = NATIVE_BEAR_MR
        return points, activity
