# Question 33: Find the common elements between two tuples.

t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

common = tuple(x for x in t1 if x in t2)
print(common)
