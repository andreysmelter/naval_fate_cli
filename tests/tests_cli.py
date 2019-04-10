import subprocess
import pytest


@pytest.mark.parametrize('interpreter, interpreter_options, cli_options, test_case', [
    ('python', '-m', '--version', '1'),
    ('python', '-m', 'ship new Guardian', '2'),
    ('python', '-m', 'ship new Guardian1 Guardian2', '3'),
    ('python', '-m', 'ship move Guardian 10 20', '4'),
    ('python', '-m', 'ship move Guardian 30 40 --speed=20', '5'),
    ('python', '-m', 'ship shoot Guardian 5 15', '6'),
    ('python', '-m', 'mine set 10 20', '7'),
    ('python', '-m', 'mine set 10 20 --drifting', '7'),
    ('python', '-m', 'mine set 10 20 --moored', '8'),
    ('python', '-m', 'mine remove 10 20', '9'),
    ('python', '-m', 'mine remove 10 20 --drifting', '9'),
    ('python', '-m', 'mine remove 10 20 --moored', '10')
])
def test_cli(impl, interpreter, interpreter_options, cli_options, test_case):
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
        '8': 'Set moored mine at [10.0,20.0]',
        '9': 'Removed drifting mine at [10.0,20.0]',
        '10': 'Removed moored mine at [10.0,20.0]'
    }
    assert result.decode('utf-8').strip() == outcomes[test_case]
