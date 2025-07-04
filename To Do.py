import os
to_dos = []
selection = "nll"


def add_item():
    to_dos.append(input("Item to add?\n    "))
    print("To do list is now \n\n",to_dos)

def check_item():
    print("err")

def remove_item():
    to_dos.remove(input("Item to remove?\n    "))

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def print_list(lst):
    ptr = 0
    while ptr < len(lst):
        print(lst[ptr])
        ptr += 1


while selection != 4:
    try:
        selection = int(input("1: Add item\n2: Check off item\n3: Remove item\n4: Exit program\n    "))
        clear()
        if selection == 1:
            add_item()
        elif selection == 2:
            check_item()
        elif selection == 3:
            remove_item()
        else:
            raise(ValueError)
        print_list(to_dos)
    except ValueError:
        print("Oops, thats not a valid choice. Try again.\n")