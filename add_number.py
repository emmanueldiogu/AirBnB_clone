#!/usr/bin/python3
"""Module for adding numbers"""


def add_numbers(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError("Both inputs must be integers.")


if __name__ == "__main__":
    print(add_numbers(3, 4))
