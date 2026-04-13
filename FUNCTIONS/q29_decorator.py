Q29. What is a decorator in Python?

A decorator adds extra behavior to a function without changing its original code.


def decorator_function(original_function):
    def wrapper():
        print('Before function call')
        original_function()
        print('After function call')
    return wrapper

@decorator_function
def say_hello():
    print('Hello')

say_hello()
