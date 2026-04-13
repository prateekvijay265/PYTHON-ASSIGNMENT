def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Division by zero is not allowed')
    return a / b

print(divide(10, 2))
