# Question 38: Create a tuple of tuples where each tuple has two elements: a number and its square.

result = tuple((i, i * i) for i in range(1, 6))
print(result)
