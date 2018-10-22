import subprocess

import pytest


@pytest.fixture(scope='function')
def put_honmaru_yml(request):
    filename = 'fixture/honmaru.yml/{0}'.format(request.param)
    subprocess.call(['cp', filename, 'honmaru.yml'])

    yield

    subprocess.call(['rm', 'honmaru.yml'])
