Q10. What is a default parameter in a Python function?

A default parameter already has a value in the function definition.
If the caller does not pass a value, the default is used.


def greet(name='Guest'):
    print('Hello', name)

greet('Aman')
greet()
