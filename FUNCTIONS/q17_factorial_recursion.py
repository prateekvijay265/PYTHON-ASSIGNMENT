Q17. Write a Python function to calculate the factorial of a number using recursion.


def factorial(n):
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
