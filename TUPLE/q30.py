# Question 30: Create a tuple of numbers and find the average using a loop.

t = (10, 20, 30, 40, 50)
total = 0
count = 0

for num in t:
    total += num
    count += 1

average = total / count
print("Average:", average)
