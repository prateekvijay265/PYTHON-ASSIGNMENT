Q43. How can you return multiple values in Python?

Return them separated by commas. Python packs them into a tuple.


def calculate(a, b):
    return a + b, a - b, a * b

sum_value, diff_value, product_value = calculate(10, 5)
print(sum_value, diff_value, product_value)
