to_dos = []
while selection != 4:
    try:
        selection = int(input("1: Add item\n2: Check off item\n3: Remove item\n4: Exit program"))
        if selection == 1:
            pass
    except ValueError:
        print("Oops, thats not a valid choice. Try again.\n")
    




def add_item():
    to_dos.append(input("Item to add?\n     "))
    print("To do list is now \n\n",to_dos)