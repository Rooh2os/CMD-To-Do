import os,json #setup
selection = "nll"
listn = 0
master = []
to_dos = []

def print_list(lst):
    global master
    global to_dos
    ptr = 0
    while ptr < len(lst):
        print(ptr,":",lst[ptr])
        ptr += 1

def write():
    global master
    global to_dos
    master[listn] = to_dos
    with open("data","w") as file:
                json.dump(master,file,indent=4)

def switch_list():
    global master
    global to_dos
    global listn
    clear()
    if ['New list'] not in master:
        master.append(['New list'])
    try:
        #print("DEBUG:",master)
        print_list(master)
        print("List to switch too?\nInput a number to select.")
        listn = int(input())
        to_dos = master[listn]
        #print("DEBUG:",to_dos)
    except(ValueError,IndexError,TypeError):
        clear()
        print("Oops, thats not a valid choice. Try again.\n")
    if "New list" in to_dos:
        #print("DEBUG:",to_dos)
        #print_list(to_dos) #DEBUG
        to_dos.remove("New list")

def add_item():
    global master
    global to_dos
    to_dos.append(input("\nItem to add?\n"))

def check_item():
    global master
    global to_dos
    try:
        print("Item to check off?\nInput a number to select.")
        item = int(input())
        to_dos[item] = to_dos[item],"[DONE]"
    except(ValueError,IndexError):
        clear()
        print("Oops, thats not a valid choice. Try again.\n")

def remove_item():
    global master
    global to_dos
    to_dos.remove(input("Item to remove?\n"))

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

try:
    with open("data","r") as file:
        master = json.load(file)
        #print("DEBUG:",master)
except(FileNotFoundError,):
    master = []
    print("No file found. Making new file")

switch_list()

while True:
    #print("DEBUG:",to_dos)
    try:
        selection = int(input("\nInput a number to select.\n1: Add item\n2: Check off item\n3: Remove item\n4: Switch list\n5: Exit program\n"))
        clear()
        print_list(to_dos)
        
        if selection == 1: #add
            add_item()

        elif selection == 2: #check item
            check_item()

        elif selection == 3: #remove item
            remove_item()

        elif selection == 4: #switch list
            switch_list()

        elif selection == 5: #exit
            write()
            break
        
        else: #trigger bad input
            raise(ValueError)
        
        clear()
        write()
        print("Your list is now:")
        print_list(to_dos)
        print("")

    except ValueError: #resolve bad input
        clear()
        print("Oops, thats not a valid choice. Try again.\n")