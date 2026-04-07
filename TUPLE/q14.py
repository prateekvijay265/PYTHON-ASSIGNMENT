# Question 14: Check if all elements in a tuple are positive using a loop.

t = (5, 8, 12, 3)
all_positive = True

for num in t:
    if num <= 0:
        all_positive = False
        break

print("All elements are positive:", all_positive)
