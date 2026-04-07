# Question 13: Access the third element of the second tuple in the nested tuple from question 12.
# The nested tuple is: ((1, 2), (3, 4), (5, 6))
# The second tuple is (3, 4), which has only 2 elements.
# So the third element does not exist.

nested_tuple = ((1, 2), (3, 4), (5, 6))

try:
    print(nested_tuple[1][2])
except IndexError:
    print("IndexError: The second tuple has no third element.")
