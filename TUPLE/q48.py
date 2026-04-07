# Question 48: Check if all elements in a tuple are even using a loop.

t = (2, 4, 6, 8, 10)
all_even = True

for num in t:
    if num % 2 != 0:
        all_even = False
        break

print("All elements are even:", all_even)
