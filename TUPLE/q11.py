# Question 11: Create a tuple using tuple comprehension that contains the squares of numbers from 1 to 5.
# Note: Python does not have direct tuple comprehension.
# We use tuple() with a generator expression.

squares = tuple(i * i for i in range(1, 6))
print(squares)
