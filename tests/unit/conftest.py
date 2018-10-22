import os
import subprocess

import pytest


@pytest.fixture(scope='function')
def put_honmaru_yml(request):
    filename = 'fixture/honmaru.yml/{0}'.format(request.param)
    subprocess.call(['cp', filename, 'honmaru.yml'])

    yield

    subprocess.call(['rm', 'honmaru.yml'])


@pytest.fixture(scope='function')
def put_environments(request):

    old_envs = {}
    for k, v in request.param.items():
        old_envs[k] = os.environ.get(k)
        os.environ[k] = v

    yield

    for k, v in old_envs.items():
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v
