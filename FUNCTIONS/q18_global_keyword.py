Q18. How do you use the global keyword to modify a global variable within a function?

Use the global keyword inside the function before changing the variable.


count = 0

def increment():
    global count
    count += 1

increment()
increment()
print(count)
