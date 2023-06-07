"""Write a program that takes a year as
input and determines if it is a leap year.

Tested my code using the following years:
LEAP YEARS;
1600
2000
1992
2400

NOT LEAP YEARS;
1700
1800
1900
2100
2200
2300
2500
2023

"""


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("What's your year? "))
if leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
