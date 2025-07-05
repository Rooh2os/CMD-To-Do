import os,json

def print_list(lst):
    ptr = 0
    while ptr < len(lst):
        print(ptr,":",lst[ptr])
        ptr += 1

if input("Open saved file? (y/n)\n") == "n":
    master_lst = []
else:
    try:
        with open("data","r") as file:
            to_dos = json.load(file)
            print("")
            print_list(to_dos)
            #print("DEBUG:",to_dos)
    except(FileNotFoundError,):
        to_dos = []
        print("Huh, it doesent seem like there is a file.")


def add_item():
    to_dos.append(input("\nItem to add?\n"))


def check_item():
    try:
        print("Item to check off?\nInput a number to select.")
        item = int(input())
        to_dos[item] = to_dos[item],"[DONE]"
    except(ValueError,IndexError):
        clear()
        print("Oops, thats not a valid choice. Try again.\n")


def remove_item():
    to_dos.remove(input("Item to remove?\nInput text to select.\n"))


def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')


selection = "nll"

while selection != 4:
    try:
        selection = int(input("\nInput a number to select.\n1: Add item\n2: Check off item\n3: Remove item\n4: Exit program\n"))
        clear()
        print_list(to_dos)
        if selection == 1:
            add_item()
        elif selection == 2:
            check_item()
        elif selection == 3:
            remove_item()
        elif selection == 4:
            if input("Do you want to save? (y/n)\n") == "n":
                break
            else:
                with open("data","w") as file:
                    json.dump(to_dos,file,indent=4)
                break
        else:
            raise(ValueError)
        clear()
        print("Your list is now:")
        print_list(to_dos)
        print("")
    except ValueError:
        clear()
        print("Oops, thats not a valid choice. Try again.\n")
        print_list(to_dos)