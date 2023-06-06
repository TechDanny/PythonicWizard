"""Create a function that receives a string as
input and checks if it starts with an uppercase letter."""


def upper():
    str = input("Type a word: ")
    if str == str.title():
        print("It is in uppercase")
    else:
        print("It is in lowercase")


upper()
