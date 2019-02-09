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


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options', [
    ('python', '-m', 'ship move Guardian 10 20'),
    ('python', '-m', 'ship move Guardian 30 40 --speed=20'),
])
def test_ship_move_cmd(impl, interpreter, interpreter_options, cli_options):
    cmd = [interpreter, interpreter_options, impl]
    cmd.extend(cli_options.split())
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    outcomes = {'Moving ship Guardian to [10.0,20.0] with speed 10.0 KN',
                'Moving ship Guardian to [30.0,40.0] with speed 20.0 KN'}
    assert result.decode('utf-8').strip() in outcomes


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options', [
    ('python', '-m', 'ship shoot Guardian 5 15')
])
def test_ship_shoot_cmd(impl, interpreter, interpreter_options, cli_options):
    cmd = [interpreter, interpreter_options, impl]
    cmd.extend(cli_options.split())
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    outcomes = {'Ship Guardian fires to [5.0,15.0]'}
    assert result.decode('utf-8').strip() in outcomes


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options', [
    ('python', '-m', 'mine set 10 20'),
    ('python', '-m', 'mine set 10 20 --drifting'),
    ('python', '-m', 'mine set 10 20 --moored'),
    ('python', '-m', 'mine remove 10 20')
])
def test_ship_shoot_cmd(impl, interpreter, interpreter_options, cli_options):
    cmd = [interpreter, interpreter_options, impl]
    cmd.extend(cli_options.split())
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    outcomes = {'Set drifting mine at [10.0,20.0]',
                'Set moored mine at [10.0,20.0]',
                'Removed mine at [10.0,20.0]'}
    assert result.decode('utf-8').strip() in outcomes
