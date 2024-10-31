import pytest
from plugins.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Test AddCommand
def test_add_command():
    add_command = AddCommand(10, 5)
    assert add_command.execute() == 15

def test_add_command_with_negative():
    add_command = AddCommand(-10, 5)
    assert add_command.execute() == -5

# Test SubtractCommand
def test_subtract_command():
    subtract_command = SubtractCommand(10, 5)
    assert subtract_command.execute() == 5

def test_subtract_command_with_negative():
    subtract_command = SubtractCommand(-10, 5)
    assert subtract_command.execute() == -15

# Test MultiplyCommand
def test_multiply_command():
    multiply_command = MultiplyCommand(10, 5)
    assert multiply_command.execute() == 50

def test_multiply_command_with_zero():
    multiply_command = MultiplyCommand(10, 0)
    assert multiply_command.execute() == 0

# Test DivideCommand
def test_divide_command():
    divide_command = DivideCommand(10, 5)
    assert divide_command.execute() == 2

def test_divide_command_by_zero():
    divide_command = DivideCommand(10, 0)
    assert divide_command.execute() == "Error: Division by zero"

def test_divide_command_with_negative():
    divide_command = DivideCommand(10, -5)
    assert divide_command.execute() == -2
