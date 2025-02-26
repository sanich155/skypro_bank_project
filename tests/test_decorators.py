import os

from src.decorators import log


def test_console_1(capsys):
    """Первый тест. Вывод в консоль успешного завершения функции"""

    @log()
    def run_success():
        """Функция для тестирования декоратора"""
        return "paint this town blue"

    run_success()
    captured = capsys.readouterr()
    assert captured.out == ("run_success ok\npaint this town blue\n")


def test_console_2(capsys):
    """Второй тест вывода в консоль. Функция завершается ошибкой"""

    @log()
    def some_err():
        """Функция для тестирования декоратора"""
        raise Exception("SOMBRERO")

    some_err()
    captured = capsys.readouterr()
    assert captured.out == ("some_err error: SOMBRERO. Inputs: (), {}\n")


def test_file_1():
    """Третий тест декоратора. Вывод в файл"""

    if os.path.exists("add.txt"):
        os.remove("add.txt")

    @log("add.txt")
    def add(x, y):
        """Функция для тестирования декоратора"""
        return x + y

    add(5, 3)
    with open("add.txt", "r") as f:
        logs = f.read()
    assert logs == "add ok\n8\n"


def test_file_2():
    """Четвертый тест для декоратора. Вывод в файл"""

    if os.path.exists("divid.txt"):
        os.remove("divid.txt")

    @log("divid.txt")
    def divid(x, y):
        """Функция для тестирования декоратора"""
        return x / y

    divid(3, 0)
    with open("divid.txt", "r") as f:
        logs = f.read()
    assert logs == "divid error: division by zero. Inputs: (3, 0), {}"
