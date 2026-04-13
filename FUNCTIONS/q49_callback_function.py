Q49. Explain the concept of a callback function in Python.

A callback function is a function passed into another function and called later.


def greet(name):
    print('Hello', name)

def process_user(callback, username):
    print('Processing user...')
    callback(username)

process_user(greet, 'Aman')
