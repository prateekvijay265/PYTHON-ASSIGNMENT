# Question 41: Create a tuple of strings and capitalize all elements using a loop.

t = ("python", "java", "c++")
capitalized_list = []

for word in t:
    capitalized_list.append(word.capitalize())

capitalized_tuple = tuple(capitalized_list)
print(capitalized_tuple)
