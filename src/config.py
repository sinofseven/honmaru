import os

import yaml


def read_honmaru_yml():
    with open('honmaru.yml') as f:
        data = yaml.load(f)
    return dict(data) if data is not None else {}


def read_environments():
    result = {}
    profile = os.environ.get('AWS_PROFILE')
    region = os.environ.get('AWS_DEFAULT_REGION')

    if profile is not None:
        result['profile'] = profile

    if region is not None:
        result['region'] = region

    return result


class Config(object):
    def __init__(self):
        read_honmaru_yml()
