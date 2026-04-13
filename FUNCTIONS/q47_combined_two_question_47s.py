Q47. This file combines both repeated Question 47 prompts from your list.

Part A: What is the purpose of the __init__ method in a Python class?
The __init__ method is a constructor that initializes object attributes.

Part B: How can you create a function that accepts a variable number of positional
and keyword arguments with defaults?
You combine normal/default parameters with *args and **kwargs.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Name:', self.name)
        print('Age:', self.age)

student1 = Student('Aman', 20)
student1.show()


def demo(a=10, b=20, *args, **kwargs):
    print('a =', a)
    print('b =', b)
    print('extra positional =', args)
    print('extra keyword =', kwargs)

demo(1, 2, 3, 4, name='Riya', city='Delhi')
