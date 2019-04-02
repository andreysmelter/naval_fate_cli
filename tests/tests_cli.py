import subprocess
import pytest


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options', [
    ('python', '-m', '--version')
])
def test_version_cmd(impl, interpreter, interpreter_options, cli_options):
    cmd = [interpreter, interpreter_options, impl, cli_options]
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    assert result.decode('utf-8').strip() == '1.0.0'


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options, test_case', [
    ('python', '-m', 'ship new Guardian', '1'),
    ('python', '-m', 'ship new Guardian1 Guardian2', '2')
])
def test_ship_new_cmd(impl, interpreter, interpreter_options, cli_options, test_case):
    cmd = [interpreter, interpreter_options, impl]
    cmd.extend(cli_options.split())
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    outcomes = {'1': 'Created ship Guardian',
                '2': 'Created ship Guardian1\nCreated ship Guardian2'}
    assert result.decode('utf-8').strip() == outcomes[test_case]


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options, test_case', [
    ('python', '-m', 'ship move Guardian 10 20', '1'),
    ('python', '-m', 'ship move Guardian 30 40 --speed=20', '2')
])
def test_ship_move_cmd(impl, interpreter, interpreter_options, cli_options, test_case):
    cmd = [interpreter, interpreter_options, impl]
    cmd.extend(cli_options.split())
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    outcomes = {'1': 'Moving ship Guardian to [10.0,20.0] with speed 10.0 KN',
                '2': 'Moving ship Guardian to [30.0,40.0] with speed 20.0 KN'}
    assert result.decode('utf-8').strip() == outcomes[test_case]


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options, test_case', [
    ('python', '-m', 'ship shoot Guardian 5 15', '1')
])
def test_ship_shoot_cmd(impl, interpreter, interpreter_options, cli_options, test_case):
    cmd = [interpreter, interpreter_options, impl]
    cmd.extend(cli_options.split())
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    outcomes = {'1': 'Ship Guardian fires to [5.0,15.0]'}
    assert result.decode('utf-8').strip() == outcomes[test_case]


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options, test_case', [
    ('python', '-m', 'mine set 10 20', '1'),
    ('python', '-m', 'mine set 10 20 --drifting', '1'),
    ('python', '-m', 'mine set 10 20 --moored', '2'),
    ('python', '-m', 'mine remove 10 20', '3'),
    ('python', '-m', 'mine remove 10 20 --drifting', '3'),
    ('python', '-m', 'mine remove 10 20 --moored', '4')
])
def test_mine_set_remove_cmd(impl, interpreter, interpreter_options, cli_options, test_case):
    cmd = [interpreter, interpreter_options, impl]
    cmd.extend(cli_options.split())
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    outcomes = {'1': 'Set drifting mine at [10.0,20.0]',
                '2': 'Set moored mine at [10.0,20.0]',
                '3': 'Removed drifting mine at [10.0,20.0]',
                '4': 'Removed moored mine at [10.0,20.0]'}
    assert result.decode('utf-8').strip() == outcomes[test_case]


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options, test_case', [
    ('python', '-m', '--version', '1'),
    ('python', '-m', 'ship new Guardian', '2'),
    ('python', '-m', 'ship new Guardian1 Guardian2', '3'),
    ('python', '-m', 'ship move Guardian 10 20', '4'),
    ('python', '-m', 'ship move Guardian 30 40 --speed=20', '5'),
    ('python', '-m', 'ship shoot Guardian 5 15', '6'),
    ('python', '-m', 'mine set 10 20', '7'),
    ('python', '-m', 'mine set 10 20 --drifting', '7'),
    ('python', '-m', 'mine set 10 20 --moored', '8')

])
def test_combined_cmd(impl, interpreter, interpreter_options, cli_options, test_case):
    cmd = [interpreter, interpreter_options, impl]
    cmd.extend(cli_options.split())
    result = subprocess.check_output(cmd, shell=False, stderr=subprocess.STDOUT)
    outcomes = {
        '1': '1.0.0',
        '2': 'Created ship Guardian',
        '3': 'Created ship Guardian1\nCreated ship Guardian2',
        '4': 'Moving ship Guardian to [10.0,20.0] with speed 10.0 KN',
        '5': 'Moving ship Guardian to [30.0,40.0] with speed 20.0 KN',
        '6': 'Ship Guardian fires to [5.0,15.0]',
        '7': 'Set drifting mine at [10.0,20.0]',
        '8': 'Set moored mine at [10.0,20.0]'
    }
    assert result.decode('utf-8').strip() == outcomes[test_case]
