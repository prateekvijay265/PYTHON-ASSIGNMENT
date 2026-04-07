# Question 43: Create a new tuple of numbers by multiplying corresponding elements of two tuples.

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

result = tuple(a * b for a, b in zip(t1, t2))
print(result)
