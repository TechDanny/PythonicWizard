"""
Creating a guessing game with python
"""


correct_number = 9
guess_limit = 3
guess_start = 0
while guess_start < guess_limit:
    guess = int(input("Guess the Number: "))
    guess_start += 1
    if guess == correct_number:
        print("You Won!")
        break
else:
    print("You lost!")
