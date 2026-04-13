Q22. Explain the purpose of *args and **kwargs parameters in a function.

*args accepts extra positional arguments as a tuple.
**kwargs accepts extra keyword arguments as a dictionary.


def demo(*args, **kwargs):
    print('args =', args)
    print('kwargs =', kwargs)

demo(1, 2, 3, name='Aman', age=20)
