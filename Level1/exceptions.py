while True:
     try:
         x = int(input("What's the value: "))
         print(f"x is {x}")
         break
     except ValueError:
         print("The value you entered is not an integer")
