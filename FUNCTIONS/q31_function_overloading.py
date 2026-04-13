Q31. Explain the concept of function overloading in Python.

Python does not support traditional function overloading directly.
Similar behavior can be achieved using default arguments, *args, or **kwargs.


def add(a, b=0, c=0):
    return a + b + c

print(add(5))
print(add(5, 10))
print(add(5, 10, 15))
