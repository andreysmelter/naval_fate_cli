import subprocess
import pytest


@pytest.mark.parametrize('interpreter, interpreter_option, cli_option', [
    ('python', '-m', '--version')
])
def test_version_cmd(impl, interpreter, interpreter_option, cli_option):
    cmd = [interpreter, interpreter_option, impl, cli_option]
    result = subprocess.check_output(cmd)
    assert result.decode('utf-8').strip() == '1.0.0'
