def fibonacci_upto(limit):
    sequence = []
    a, b = 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci_upto(50))
