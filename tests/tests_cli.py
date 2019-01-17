import subprocess
import pytest


@pytest.mark.parametrize('interpreter, interpreter_option, cli_option', [
    ('python', '-m', '--version')
])
def test_version_cmd(impl, interpreter, interpreter_options, cli_options):
    cmd = [interpreter, interpreter_options, impl, cli_options]
    result = subprocess.check_output(cmd)
    assert result.decode('utf-8').strip() == '1.0.0'


# @pytest.mark.parametrize('interpreter, cli, option', [
#     ('python', 'naval_fate.py', '--version')
# ])
# def test_ship_new_cmd(impl, interpreter, cli, option):
#    pass
