import subprocess


def test_version_cmd(impl):
    cmd = ['python', '{}/naval_fate.py'.format(impl), '--version']
    result = subprocess.check_output(cmd)
    assert result.decode('utf-8').strip() == '1.0.0'
