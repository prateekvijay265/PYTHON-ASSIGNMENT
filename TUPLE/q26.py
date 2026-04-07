# Question 26: Merge two tuples and remove any duplicates.

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
merged_unique = tuple(dict.fromkeys(t1 + t2))
print(merged_unique)
