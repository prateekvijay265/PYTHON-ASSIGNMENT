Q37. Explain the concept of a recursive function with a base case.

A base case stops recursion and prevents infinite recursive calls.


def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(5))
