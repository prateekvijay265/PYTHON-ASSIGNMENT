Q7. Explain the concept of a return statement in a function.

The return statement sends a value back to the caller and ends function execution.
If no return statement is used, Python returns None.


def square(n):
    return n * n

result = square(6)
print(result)
