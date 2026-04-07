# Question 44: Convert a list of strings into a tuple of uppercase strings using a loop.

words = ["apple", "banana", "cherry"]
upper_list = []

for word in words:
    upper_list.append(word.upper())

upper_tuple = tuple(upper_list)
print(upper_tuple)
