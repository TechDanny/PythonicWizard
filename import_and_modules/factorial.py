"""
Create a Python module that contains a function to calculate the factorial of a given number. Import this module into another script and use the factorial function to calculate the factorial of a user-provided number.
"""


from factorial_helper import factorial


num = int(input("What's your number: "))
number = factorial(num)
print(f"The factorial of {num} is: {number}")
