""""
calculates sum of factorial and two values
"""


from calc_math import add
from factorial_helper import factorial


number = int(input("Enter your desired number: "))
value1 = int(input("Enter value 1: "))
value2 = int(input("Enter value 2: "))
total_sum = add(value1, value2) + factorial(number)
print(f"Sum of factorial number {number} and the two values is:")
print(f"{add(value1, value2)} + {factorial(number)} = {total_sum}")

