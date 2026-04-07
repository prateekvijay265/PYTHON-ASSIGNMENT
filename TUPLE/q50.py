# Question 50: Create a new tuple with elements from two tuples, but remove duplicates.

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

result = tuple(dict.fromkeys(t1 + t2))
print(result)
