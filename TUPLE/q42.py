# Question 42: Find the index of the last occurrence of a specific element in a tuple.

t = (1, 2, 3, 2, 4, 2, 5)
element = 2
last_index = len(t) - 1 - t[::-1].index(element)
print("Last occurrence index:", last_index)
