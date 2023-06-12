command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("The car has started")
    elif command == "stop":
        print("The car has stopped")
    elif command == "quit":
        print("The program has been terminated")
    elif command == "help":
        print("""
        1. start: starting engine
        2. stop: engine
        3. quit: to exit
         """)
    else:
        print("Invalid")
