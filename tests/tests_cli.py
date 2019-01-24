import subprocess
import pytest


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options', [
    ('python', '-m', '--version')
])
def test_version_cmd(impl, interpreter, interpreter_options, cli_options):
    cmd = [interpreter, interpreter_options, impl, cli_options]
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    assert result.decode('utf-8').strip() == '1.0.0'


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options', [
    ('python', '-m', 'ship new Guardian'),
    ('python', '-m', 'ship new Guardian1 Guardian2')
])
def test_ship_new_cmd(impl, interpreter, interpreter_options, cli_options):
   cmd = [interpreter, interpreter_options, impl]
   cmd.extend(cli_options.split())
   result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
   list_of_ships = [word for word in result.decode('utf-8').split() if word.startswith('Guardian')]
   assert list_of_ships == ['Guardian'] or list_of_ships == ['Guardian1', 'Guardian2']
