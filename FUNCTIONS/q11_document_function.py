Q11. How do you document a function in Python?

A function is usually documented with a docstring written inside triple quotes
just below the function header.


def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add.__doc__)
