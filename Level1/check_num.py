"""Write a Python program that takes a number as
input and checks if it is positive, negative, or zero.
"""

num = int(input("Enter a value: "))
if num < 0:
    print(f"{num} is negative")
elif num == 0:
    print(f"{num} is zero")
else:
    print(f"{num} is positive")
