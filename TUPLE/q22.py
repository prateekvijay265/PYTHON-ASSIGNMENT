# Question 22: Create a new tuple that contains elements from two tuples in pairs.

t1 = (1, 2, 3)
t2 = ("a", "b", "c")
paired_tuple = tuple(zip(t1, t2))
print(paired_tuple)
