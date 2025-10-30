import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide   # Import the Operations class from the operations module

Num = Union[int, float]


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 8),           # Test adding two positive integers
        (0, 0, 0),           # Test adding two zeros
        (-5, 3, -2),         # Test adding a negative and a positive integer
        (-5, -3, -8),        # Test adding negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]
)
def test_addition(a: Num, b: Num, expected: Num) -> None:
    result = add(a, b)
    
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

# ---------------------------------------------
# Unit Tests for the 'subtraction' Method
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting two positive integers
        (3, 5,-2),           # Test subtracting a smaller positive integer from a larger one
        (0, 0, 0),           # Test subtracting two zeros
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (3, -5, 8),          # Test subtracting positive integer from another negative integer
        (10.5, 5.5, 5.0),    # Test subtracting two positive floats
        (-10.5, -5.5, -5.0), # Test subtracting two negative floats
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_smaller_positive_integer_from_larger",
        "subtract_two_zeros",
        "subtract_negative_integer_from_negative_integer",
        "subtract_negative_integer_from_positive_integer",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
    ]
)
def test_subtraction(a: Num, b: Num, expected: Num) -> None:
    result = subtract(a, b)
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a positive and negative integers
        (0, 10, 0),          # Test multiplying zero with a positive integer
        (-2, -3, 6),         # Test multiplying two negative integers
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_positive_and_negative_integers",
        "multiply_zero_with_positive_integer",
        "multiply_two_negative_integers",
        "multiply_two_positive_floats",
        "multiply_negative_float_with_positive_float",
    ]
)
def test_multiplication(a: Num, b: Num, expected: Num) -> None:
    result = multiply(a, b)
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, -3, 2.0),         # Test dividing two negative integers
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_division(a: Num, b: Num, expected: float) -> None:
    result = divide(a, b)
    
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),    # Test dividing by zero with positive dividend
        (-1, 0),   # Test dividing by zero with negative dividend
        (0, 0),    # Test dividing zero by zero
    ],
    ids=[
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero",
    ]
)
def test_division_by_zero(a: Num, b: Num) -> None:

    with pytest.raises(ValueError, match="Cannot divide by zero!") as excinfo:
        # Attempt to divide 'a' by 'b', which should raise a ValueError
        divide(a, b)
    
    # Assert that the exception message contains the expected error message
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"

