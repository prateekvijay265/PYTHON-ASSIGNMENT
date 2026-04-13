Q24. Define a generator function in Python.

A generator function uses yield and returns values one by one.


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(5):
    print(value)
