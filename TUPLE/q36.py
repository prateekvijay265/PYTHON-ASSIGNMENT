# Question 36: Create a tuple of numbers and find the largest odd number using a loop.

t = (12, 7, 18, 21, 5, 14)
largest_odd = None

for num in t:
    if num % 2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

print("Largest odd number:", largest_odd)
