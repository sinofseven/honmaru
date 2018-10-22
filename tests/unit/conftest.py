import subprocess

import pytest


@pytest.fixture(scope='function')
def put_honmaru_yml(request):
    def delete_file():
        subprocess.call(['rm', 'honmaru.yml'])

    filename = 'fixture/honmaru.yml/{0}'.format(request.param)
    subprocess.call(['cp', filename, 'honmaru.yml'])

    request.addfinalizer(delete_file)
