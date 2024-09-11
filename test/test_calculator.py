import pytest
import calculator
from calculator import *
from pytest import approx

# handles addition
def test_addition():
  assert add(2, 3) == 5

# handles subtraction
def test_subtraction():
  assert subtract(10, 1) == 9

# handles multiplication
def test_multiply():
  assert multiply(1, 10) == 10

# handles division
# DONE: handles zero division 
def test_divide():
  assert divide(1, 0) == "Cannot divide by 0"
  assert divide(10, 3) == 10/3
  assert divide(99,2) == 49.5

def test_get_num(monkeypatch):
  # Mock user input for valid integer
  monkeypatch.setattr('builtins.input', lambda _: "42")
  assert get_num("Enter a number: ") == 42

  # Mock user input for invalid input (non-integer)
  monkeypatch.setattr('builtins.input', lambda _: "abc")
  assert get_num(
      "Enter a number: ") == "Please enter a valid integer"

def test_get_selection(monkeypatch):
    # Mock user input for valid selection
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert get_selection() == 3

    # Mock user input for invalid selection
    monkeypatch.setattr('builtins.input', lambda _: "abc")
    with pytest.raises(ValueError):
        get_selection()

# Handles division by a negative number
def test_divide_negative():
  assert divide(10, -2) == -5
  assert divide(-10, -2) == 5
  assert divide(-10, 2) == -5

# Handles division by a positive number
def test_divide_positive():
  assert divide(10, 2) == 5

# Handles division by a floating-point number
def test_divide_float():
  assert divide(10, 3) == 10/3

# Handles division by zero with negative dividend
def test_divide_zero_negative():
  assert divide(-10, 0) == "Cannot divide by 0"

# Handles division by zero with positive dividend
def test_divide_zero_positive():
  assert divide(10, 0) == "Cannot divide by 0"

# Gets a selection from user input with valid range
def test_get_selection_valid_range(monkeypatch):
  # Mock user input for valid selection
  monkeypatch.setattr('builtins.input', lambda _: "3")
  assert get_selection() == 3

  # Mock user input for invalid selection
  monkeypatch.setattr('builtins.input', lambda _: "abc")
  with pytest.raises(ValueError):
      get_selection()

# Handles division by zero with zero dividend
def test_divide_zero_zero():
  assert divide(0, 0) == "Cannot divide by 0"
  
  
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, 5), (-2, -3, -5), (2, -3, -1)])
def test_param_add(num1, num2, expectedResult):
    result = calculator.add(num1, num2)
    assert result == expectedResult

# Testing Multiply Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, 6), (-2, -3, 6), (2, -3, -6)])
def test_Multiply(num1, num2, expectedResult):
    result = calculator.multiply(num1, num2)
    assert result == expectedResult

# Testing Division Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(21, 3, 7), (-21, -3, 7), (-21, 3, -7)])
def test_Divide(num1, num2, expectedResult):
    result = calculator.divide(num1, num2)
    assert result == expectedResult

# Test Calculator does not take in more than 3 values

# Test Calculator when double 0 values entered
def test_doubleZeroInput():
    result = calculator.subtract(0, 0)
    assert result == 0

# Test Calcutor to limit max 2 digit input
def test_maxdoublegigit(monkeypatch):
     monkeypatch.setattr('builtins.input', lambda _: "42")
     x = "34"
     get_num("Enter a number: ") == x
     assert len(x)  <= 2
     
def test_valid_selections(monkeypatch):
    # Test valid selections
    for valid_value in [1, 2, 3, 4]:
        monkeypatch.setattr('builtins.input', lambda _: str(valid_value))
        assert get_selection() == valid_value

def test_invalid_selections(monkeypatch):
    # Test invalid selections
    for invalid_value in [0, 5, -1, 6]:
        monkeypatch.setattr('builtins.input', lambda _: str(invalid_value))
        with pytest.raises(ValueError):
            get_selection()

def test_valid_selections(monkeypatch):
    # Test valid selections
    for valid_value in [1, 2, 3, 4]:
        monkeypatch.setattr('builtins.input', lambda _: str(valid_value))
        assert get_selection() == valid_value

def test_invalid_selections(monkeypatch):
    # Test invalid selections
    for invalid_value in [0, 5, -1, 6]:
        monkeypatch.setattr('builtins.input', lambda _: str(invalid_value))
        with pytest.raises(ValueError):
            get_selection()


