from config import Config


class TestConfig(object):
    def test_not_exist_honmaru_yml(self):
        Config()
