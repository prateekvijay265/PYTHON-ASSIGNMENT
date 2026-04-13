Q13. How can you make a function accept a variable number of arguments?

Use *args to accept any number of positional arguments.
Python stores them as a tuple.


def total(*args):
    s = 0
    for value in args:
        s += value
    return s

print(total(1, 2, 3))
print(total(10, 20, 30, 40))
