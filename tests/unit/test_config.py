import pytest

from config import Config


class TestConfig(object):
    def test_not_exist_honmaru_yml(self):
        with pytest.raises(FileNotFoundError):
            Config()

    @pytest.mark.parametrize(
        'put_honmaru_yml', [
            ('init.yml')
        ], indirect=True
    )
    def test_exist_file(self, put_honmaru_yml):
        Config()
