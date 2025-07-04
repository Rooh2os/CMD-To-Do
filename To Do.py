import os,json

def print_list(lst):
    ptr = 0
    while ptr < len(lst):
        print(ptr,":",lst[ptr])
        ptr += 1

to_dos = []
if input("Open saved file? (y/n)\n") == "n":
    to_dos = []
else:
    try:
        with open("data","r") as file:
            to_dos = json.load(file)
            print_list(to_dos)
            #print("DEBUG:",to_dos)
    except(FileNotFoundError,):
        to_dos = []
        print("Huh, there doesent seem like there is a file.")
selection = "nll"


def add_item():
    to_dos.append(input("Item to add?\n"))

def check_item():
    try:
        print("Item to check off?")
        print_list(to_dos)
        item = int(input())
        to_dos[item] = to_dos[item],"[DONE]"
    except(ValueError,IndexError):
        clear()
        print("Oops, thats not a valid choice. Try again.\n")

def remove_item():
    to_dos.remove(input("Item to remove?\n"))

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')




while selection != 4:
    try:
        selection = int(input("1: Add item\n2: Check off item\n3: Remove item\n4: Exit program\n"))
        clear()
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
        print("Your list is now:")
        print_list(to_dos)
        print("\n")
    except ValueError:
        clear()
        print("Oops, thats not a valid choice. Try again.\n")
        print_list(to_dos)