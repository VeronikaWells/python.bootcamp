user_input = ''
while True:
    menu = """Please select an option below:
1: Option 1
2: Option 2
3: Option 3
4: Quit
"""
    user_input = input(menu)
    if user_input == "1":
        print("Option 1 chosen")
    elif user_input == "2":
        print("Option 2 chosen")
    elif user_input == "3":
        print("Option 3 chosen")
    elif user_input == "4":
        print("Goodbye.")
        break
    else:
        print("No menu option selected")