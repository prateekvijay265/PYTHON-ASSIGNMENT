Q19. What is variable scope in Python?

Scope is the region where a variable can be accessed.
Python follows LEGB: Local, Enclosing, Global, Built-in.


x = 'global'

def outer():
    y = 'enclosing'
    def inner():
        z = 'local'
        print(z)
        print(y)
        print(x)
    inner()

outer()
