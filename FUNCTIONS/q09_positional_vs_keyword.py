Q9. What is the difference between positional and keyword arguments?

Positional arguments are matched by order.
Keyword arguments are matched by parameter name.


def show(name, age):
    print(name, age)

show('Aman', 20)
show(age=20, name='Aman')
