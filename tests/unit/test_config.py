import pytest

from config import Config, read_environments, read_honmaru_yml


class TestReadHonmaruYml(object):
    def test_not_exist_honmaru_yml(self):
        with pytest.raises(Exception):
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
        with pytest.raises(Exception):
            Config()

    @pytest.mark.parametrize(
        'put_honmaru_yml, put_environments, profile, region', [
            (
                'empty.yml',
                {},
                None,
                None
            ),
            (
                'empty.yml',
                {
                    'AWS_PROFILE': 'dummy-profile-1',
                    'AWS_DEFAULT_REGION': 'eu-west-1'
                },
                'dummy-profile-1',
                'eu-west-1'
            ),
            (
                'empty.yml',
                {
                    'AWS_PROFILE': 'dummy-profile-2'
                },
                'dummy-profile-2',
                None
            ),
            (
                'empty.yml',
                {
                    'AWS_DEFAULT_REGION': 'eu-west-2'
                },
                None,
                'eu-west-2'
            ),
            (
                'config_1.yml',
                {},
                'test-profile-1',
                'ap-northeast-1'
            ),
            (
                'config_1.yml',
                {
                    'AWS_PROFILE': 'dummy-profile-1',
                    'AWS_DEFAULT_REGION': 'us-east-1'
                },
                'dummy-profile-1',
                'us-east-1'
            ),
            (
                'config_1.yml',
                {
                    'AWS_PROFILE': 'dummy-profile-2'
                },
                'dummy-profile-2',
                'ap-northeast-1'
            ),
            (
                'config_1.yml',
                {
                    'AWS_DEFAULT_REGION': 'us-east-2'
                },
                'test-profile-1',
                'us-east-2'
            ),
            (
                'config_2.yml',
                {},
                'test-profile-2',
                None
            ),
            (
                'config_2.yml',
                {
                    'AWS_PROFILE': 'dummy-profile-1',
                    'AWS_DEFAULT_REGION': 'ap-northeast-1'
                },
                'dummy-profile-1',
                'ap-northeast-1'
            ),
            (
                'config_2.yml',
                {
                    'AWS_PROFILE': 'dummy-profile-2'
                },
                'dummy-profile-2',
                None
            ),
            (
                'config_2.yml',
                {
                    'AWS_DEFAULT_REGION': 'ap-northeast-2'
                },
                'test-profile-2',
                'ap-northeast-2'
            )
        ], indirect=['put_honmaru_yml', 'put_environments']
    )
    def test_expected(self, put_honmaru_yml, put_environments, profile, region):
        actual = Config()
        assert actual.profile == profile
        assert actual.region == region
