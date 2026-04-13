Q34. What is the purpose of the __main__ block in Python?

It runs code only when the file is executed directly, not when imported.


def greet():
    print('Hello')

if __name__ == '__main__':
    greet()
