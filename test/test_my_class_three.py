import pytest
from python.my_class_three import Employee

def test_employee_name_setter_getter():
    e = Employee()
    e.name = "Harry"
    assert e.name == "Harry"

def test_class_attribute_show(capsys):
    e = Employee()
    e.a = 45
    e.name = "Sam"
    e.show()
    captured = capsys.readouterr()
    assert "The class attribute of a is 1" in captured.out  # class attr stays 1, not 45
