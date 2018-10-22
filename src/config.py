import yaml


def read_honmaru_yml():
    with open('honmaru.yml') as f:
        data = yaml.load(f)
    return dict(data) if data is not None else {}


class Config(object):
    def __init__(self):
        read_honmaru_yml()
