# initialize / Environment variables
import os
try:
    from configparser import ConfigParser
except ImportError:
    # Legacy ConfigParser support
    from ConfigParser import ConfigParser
INDEX_USER_NO = 0
INDEX_USER_NAME = 1
INDEX_ITEM_NAME = 0
INDEX_USER_BORROW_RECORD = 0
FUNCTION_BORROW_ITEM = 0
FUNCTION_RETURN_ITEM = 1
DISPLAY_USER_RECORDS = 2
DISPLAY_ALL_RECORDS = 3
working_directory = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
# Initialize config
config = ConfigParser()
config.read(working_directory + '/config.ini')

# you may implement other necessary functions here
# def checkWindows():
#     return (("win" in sys.platform.lower()) or ("windows" in sys.platform.lower()))

def display():
    print("Invnentory Management System")
    print(f"No. ")
    display_function_list = ("Borrow Item", "Return Item", "Display User Records", "Display All Records")
    for runtime in range(len(display_function_list)):
        print(f"{runtime:<3} | {display_function_list[runtime]}")
    try:
        return int(input(f"Please input your choice. (0-{len(display_function_list)-1}, Enter to return) : "))
    except:
        print("error")
        display()

def display_borrowed(user_name = ""):
    if not user_name == "":
        user_no = int(user_list_by_name.get(str(user_name)))
        print()
        print(f"Item No. | Item Name                                  | Qty. borrowed")
        for data in get_borrowed_list():
            item_data = data.split(", ")
            item_name = str(ITEMS[int(item_data[1])][0] + " - " + ITEMS[int(item_data[1])][1])
            if user_no == int(item_data[0]):
                print(f"{item_data[1]:>7}. | {item_name:<42} | {item_data[2]:>13}")
        print()
    else:
        print()
        print(f"Item No. | Item Name                                  | borrower   | Qty. borrowed")
        for data in get_borrowed_list():
            item_data = data.split(", ")
            item_name = str(ITEMS[int(item_data[1])][0] + " - " + ITEMS[int(item_data[1])][1])
            print(f"{item_data[1]:>7}. | {item_name:<42} | {user_list[int(item_data[0])]:<10} | {item_data[2]:>13}")
        print()

# a function remaining_quantity which accepts one parameter(UniqueItemNo)
def remaining_quantity(item_no):
    return int(tuple(ITEMS[item_no])[2]) - get_borrowed_quantity(item_no)

# a function remaining_quantity which accepts two parameter(UniqueItemNo, UniqueUserNo)
# if only one parameter were giving the, It would mean getting borrowed quantity for all user
def get_borrowed_quantity(item_no, *user_no):
    borrowed_quantity = int(0)
    for borrowed_item in get_borrowed_list():
        item = borrowed_item.split(", ")
        if user_no in locals():
            if (int(item[1]) == item_no) and (int(item[0]) == user_no):
                borrowed_quantity += int(item[2])
        else:
            if (int(item[1]) == item_no):
                borrowed_quantity += int(item[2])
    return borrowed_quantity

def get_borrowed_list():
    # ---Loading item data(txt) - Start---
    if (config.get("storage", "borrowed") == "txt"):
        raw_borrowed = str()
        for read in open(working_directory + "/data/borrowed.txt", "r"):
            if not (read.startswith("# ") or (read == "\n")): raw_borrowed += read
        return raw_borrowed.split("\n")
    # ---Loading item data(txt) - End---

# write a function items_in_stock to display the main menu
def items_in_stock():
    # complete your function here
    # this function have no return value
    print(f"Item No. | Item Name                                  | Qty. Left")
    for runtime in range(len(ITEMS)):
        item_name = str(ITEMS[runtime][0] + " - " + ITEMS[runtime][1])
        print(f"{runtime:>7}. | {item_name:<42} | {remaining_quantity(runtime):>9}")

# write a function items_borrowed which accepts one parameter(UniqueUserNo)
def items_borrowed(borrower_no):
    results = list()
    for items_borrowed in get_borrowed_list():
        data = items_borrowed.split(", ")
        if (int(data[0]) == borrower_no):
            results.append(data)
    return results

def items_borrow(borrower_name, item_no, item_quantity):
    user_no = int(user_list_by_name.get(str(borrower_name)))
    # ---Writing item data(txt) - Start---
    if (config.get("storage", "item") == "txt"):
        file = open(working_directory + "/data/borrowed.txt", "a")
        file.write(str(f"\n{user_no}, {item_no}, {item_quantity}"))
        file.close()
    # ---Writing item data(txt) - End---

def main():
    # ---Initialize - Start---
    # Assign global variables
    global user_list, user_list_by_name, user_borrow_record, ITEMS
    # Assign variables
    user_list = dict() ; user_list_by_name = dict() ;  user_borrow_record = dict() ; ITEMS = tuple()
    # ---Loading user data(txt) - Start---
    if (config.get("storage", "user") == "txt"):
        sub_user_list = list()
        for user in open(working_directory + "/data/borrowers.txt", "r"):
            if not (user.startswith("# ") or (user == "\n")): sub_user_list.append(user.rstrip("\n").split(", "))
        for runtime in range(len(sub_user_list)):
            user_list[runtime] = str(sub_user_list[runtime][0]).lower()
            user_list_by_name[str(sub_user_list[runtime][0]).lower()] = runtime
    # ---Loading user data(txt) - End---
    # ---Loading item data(txt) - Start---
    if (config.get("storage", "item") == "txt"):
        raw_ITEMS = str() ; sub_ITEMS = tuple() ; ITEMS = list()
        for read in open(working_directory + "/data/items.txt", "r"):
            if not (read.startswith("# ") or (read == "\n")): raw_ITEMS += read
        raw_ITEMS = raw_ITEMS.split("\n")
        for runtime in range(len(raw_ITEMS)):
            sub_ITEMS += tuple(raw_ITEMS[runtime].split(", "))
            if (len(sub_ITEMS) == 3):
                ITEMS.append(tuple(sub_ITEMS))
                sub_ITEMS = ()
        ITEMS = tuple(ITEMS)
    # ---Loading item data(txt) - End---
    # ---Initialize - End---
    print("Welcome to Invnentory Management System.")
    while True:
        # display inventory management system menu and ask for user input
        input_function = display()
        # When user input 0 to borrow item
        if input_function == FUNCTION_BORROW_ITEM:
            # your logics for user selected borrow item function here
            print("")
            items_in_stock()
            ask_borrow_item = int(input(f"Please input the item no. to borrow (0 - {len(ITEMS)-1}, Enter to return): "))
            ask_borrow_quantity = int(input(f"Please input the quantity to borrow, Enter to return: "))
            if (ask_borrow_quantity - get_borrowed_quantity(ask_borrow_item)) <= 0:
                print("Your input is over our item stock")

            ask_borrow_user = input(f"Please input borrower's name, Enter to return: ").lower()
            items_borrow(ask_borrow_user, ask_borrow_item, ask_borrow_quantity)
            display_borrowed(ask_borrow_user)



        # When user input 1 to return item
        elif input_function == FUNCTION_RETURN_ITEM:
            # your logics for user selected return item function here
            pass

        # When user input 2 to display a particular borrower's record
        elif input_function == DISPLAY_USER_RECORDS:
            # your logics for user selected display borrower's record here
            display_borrowed(input(f"Please input borrower's name, Enter to return: ").lower())

        # When user input 3 to display all records
        elif input_function == DISPLAY_ALL_RECORDS:
            # your logics for user selected display all records here
            display_borrowed()
