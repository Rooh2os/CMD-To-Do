import os
to_dos = []
selection = "nll"


def add_item():
    to_dos.append(input("Item to add?\n    "))

def check_item():
    item = input("Item to check off?")
    to_dos[item] = to_dos[item],"[DONE]"

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
        print("    ",lst[ptr])
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
        elif selection == 4:
            break
        else:
            raise(ValueError)
        print("Your list is now:\n")
        print_list(to_dos)
    except ValueError:
        print("Oops, thats not a valid choice. Try again.\n")