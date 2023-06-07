"""Create a function that takes two numbers as
input and returns their sum.
"""


def sum(a, b):
    return a + b


x = int(input("first value: "))
y = int(input("Second value: "))
add_values = sum(x, y)
print(f"{x} + {y} = {add_values}")
