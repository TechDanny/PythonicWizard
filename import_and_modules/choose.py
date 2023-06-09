"""
Here I'm using the in-built modules that come with python
So write a code that picks a random name from a list
"""


import random

list_names = []
num = int(input("Enter the number of names you want: "))
for i in range(num):
    names = input(f"Type the names you have {i + 1}: ")
    list_names.append(names)

choose = random.choice(list_names)
print() #i want to get an extra line
print(f"{choose} you are going to pay the bills today:):)")
