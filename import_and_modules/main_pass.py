"""
Writing a python program that generates a random password
"""
from func_pass import get_password


my_len = int(input("Enter the length of your password: "))
password = get_password(my_len)
print()
print(f"Your password is: {password}")
