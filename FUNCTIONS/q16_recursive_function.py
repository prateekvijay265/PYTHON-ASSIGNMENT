Q16. What is a recursive function in Python?

A recursive function is a function that calls itself.
It must have a base case to stop recursion.


def countdown(n):
    if n == 0:
        print('Done')
        return
    print(n)
    countdown(n - 1)

countdown(5)
