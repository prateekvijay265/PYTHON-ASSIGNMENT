# Question 40: Convert a tuple into a dictionary where each element becomes a key-value pair.
# Here the tuple contains pairs, and each pair becomes one key-value item in the dictionary.

t = (("name", "Alice"), ("age", 21), ("city", "Delhi"))
result = dict(t)
print(result)
