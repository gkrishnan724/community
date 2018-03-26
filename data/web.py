from community.git import get_org_name


def web_url():
    url = 'https://webservices.' + get_org_name() + '.io/'
    return url
