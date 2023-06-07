"""
Create a function that takes a string as
input and returns the reversed version of the string.
"""
#used the built-in method for reversing string in python


def reverse_string(name):
    return name[::-1]


string = input("Enter a string: ")
reverse = reverse_string(string)
print(reverse)
