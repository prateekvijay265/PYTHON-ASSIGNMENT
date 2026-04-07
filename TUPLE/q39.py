# Question 39: Check if all elements in a tuple are unique.

t = (1, 2, 3, 4, 5)
all_unique = len(t) == len(set(t))
print("All elements are unique:", all_unique)
