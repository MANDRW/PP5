"""Simple calculator utility module."""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference between a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the result of dividing a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def binary_convert(num: int) -> str:
    """Convert an integer to its binary representation."""
    if not isinstance(num, int):
        return "Only integers are allowed"
    if num < 0:
        return "Negative numbers are not allowed"
    if num > 100:
        return "Number too large"
    return bin(num)[2:]
