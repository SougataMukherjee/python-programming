import pytest
from python.my_decorator import my_decorator

def test_my_decorator_output(capsys):
    @my_decorator
    def sample_func():
        print("Hello!")

    sample_func()

    captured = capsys.readouterr()
    assert "Before function call" in captured.out
    assert "Hello!" in captured.out
    assert "After function call" in captured.out
