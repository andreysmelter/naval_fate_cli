import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--impl', action='store', default='docopt_cli', help='What cli implementation to use?'
    )


@pytest.fixture
def impl(request):
    return request.config.getoption('--impl')
