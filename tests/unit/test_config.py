import pytest

from config import Config, read_environments, read_honmaru_yml


class TestReadHonmaruYml(object):
    def test_not_exist_honmaru_yml(self):
        with pytest.raises(FileNotFoundError):
            read_honmaru_yml()

    @pytest.mark.parametrize(
        'put_honmaru_yml, expected', [
            (
                'empty.yml',
                {}
            ),
            (
                'read_1.yml',
                {
                    'int': 1,
                    'bool': True,
                    'str': 'tttt',
                    'array': [1, 2, 3],
                    'dict': {
                        'int': 1,
                        'bool': True,
                        'str': 'tttt'
                    }
                }
            ),
            (
                'read_2.yml',
                {
                    'profile': 'test-profile',
                    'region': 'ap-northeast-1'
                }
            )
        ], indirect=['put_honmaru_yml']
    )
    def test_exist_file(self, put_honmaru_yml, expected):
        actual = read_honmaru_yml()
        assert actual == expected


class TestReadEnvironments(object):
    @pytest.mark.parametrize(
        'put_environments, expected', [
            (
                {}, {}
            ),
            (
                {'SHELL': 'bash'}, {}
            ),
            (
                {'AWS_PROFILE': 'test-profile-1'},
                {'profile': 'test-profile-1'}
            ),
            (
                {
                    'AWS_PROFILE': 'test-profile-2',
                    'AWS_DEFAULT_REGION': 'ap-northeast-1'
                },
                {
                    'profile': 'test-profile-2',
                    'region': 'ap-northeast-1'
                }
            ),
            (
                {
                    'AWS_PROFILE': 'test-profile-3',
                    'AWS_DEFAULT_REGION': 'ap-northeast-2',
                    'SHELL': 'bash'
                },
                {
                    'profile': 'test-profile-3',
                    'region': 'ap-northeast-2'
                }
            )
        ], indirect=['put_environments']
    )
    def test_expected(self, put_environments, expected):
        actual = read_environments()
        assert actual == expected


class TestConfig(object):
    def test_not_exist_honmaru_yml(self):
        with pytest.raises(FileNotFoundError):
            Config()

    @pytest.mark.parametrize(
        'put_honmaru_yml', [
            ('empty.yml')
        ], indirect=['put_honmaru_yml']
    )
    def test_exist_file(self, put_honmaru_yml):
        Config()
