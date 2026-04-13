Q15. Explain the difference between a global and a local variable in a function.

A global variable is declared outside a function and can be accessed widely.
A local variable is declared inside a function and exists only there.


x = 'global value'

def demo():
    y = 'local value'
    print(x)
    print(y)

demo()
print(x)
