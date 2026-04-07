# Question 10: Create a tuple of even numbers from 2 to 10 using a loop.

even_list = []

for i in range(2, 11):
    if i % 2 == 0:
        even_list.append(i)

even_tuple = tuple(even_list)
print(even_tuple)
