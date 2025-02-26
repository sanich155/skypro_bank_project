import os
from src.decorators import log

def test_console_1(capsys):
    @log()
    def run_success():
        return ('paint this town blue')

    run_success()
    captured = capsys.readouterr()
    assert captured.out == (f'run_success ok\n'
                        f'paint this town blue\n')

def test_console_2(capsys):
    @log()
    def divid(x, y):
        return x / y

    @log()
    def some_err():
        raise Exception('SOMBRERO')

    some_err()
    captured = capsys.readouterr()
    assert captured.out == ('some_err error: SOMBRERO. Inputs: (), {}\n')

def test_file_1():

    if os.path.exists('add.txt'):
        os.remove('add.txt')
    @log('add.txt')
    def add(x, y):
        return x + y

    add(5 ,3)
    with open('add.txt', 'r') as f:
        logs = f.read()
    assert logs == 'add ok\n8\n'


def test_file_2():

    if os.path.exists('divid.txt'):
        os.remove('divid.txt')
    @log('divid.txt')
    def divid(x, y):
        return x / y

    divid(3, 0)
    with open('divid.txt', 'r') as f:
        logs = f.read()
    assert logs == 'divid error: division by zero. Inputs: (3, 0), {}'

