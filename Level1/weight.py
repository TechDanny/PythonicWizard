"""
This project is a Weight converter written in python,
It prompts the user for his/her weight and changes it to either pounds or kilograms
"""


weight = float(input("What's your weight: "))
weight_converter = input("L for pounds\nK for kilograms\nYou entered your weight in: ")
if weight_converter in ["L", "l"]:
    weight_in_kg = weight / 2.20462
    print(f"Your weight is: {weight_in_kg}kg")
elif weight_converter in ["K", "k"]:
    weight_in_lbs = weight * 2.20462
    print(f"Your weight is: {weight_in_lbs} pounds")
else:
    print("Invalid value!")

