import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--impl', action='store', default='docopt', help=''
    )


@pytest.fixture
def impl(request):
    return request.config.getoption('--impl')
