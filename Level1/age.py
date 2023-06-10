first_name = input("Your first name: ").title()
surname = input("your surname: ").title()
last_name = input("your last name: ").title()
day = int(input("Day of birth: "))
month = int(input("Month of birth: "))
year = int(input("Year of birth: "))
current_year = int(input("Current Year: "))
nationality = input("Country of birth: ").title()
age = current_year - year
print()
full_name = first_name + " " + surname + " " + last_name
print(f"Name: {full_name}")
print(f"Citizenship: {nationality}")
print(f"Date of birth: {day}-{month}-{year}")
print(f"You are: {age} years old")
print()
adult = 18
if age >= adult:
    print(f"Hello {last_name}, you are eligible to vote")
else:
    print(f"Hello {last_name}, you can't vote, you are still young")
