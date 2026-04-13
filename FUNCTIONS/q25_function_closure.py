Q25. Explain the concept of a function closure in Python.

A closure remembers values from its enclosing scope even after the outer function ends.


def outer(message):
    def inner():
        print(message)
    return inner

func = outer('Hello from closure')
func()
