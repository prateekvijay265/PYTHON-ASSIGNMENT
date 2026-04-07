# Question 31: Convert a list of tuples into a list of their first elements.

list_of_tuples = [(1, "a"), (2, "b"), (3, "c")]
first_elements = [item[0] for item in list_of_tuples]
print(first_elements)
