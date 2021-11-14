# initialize / Environment variables
import os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
ITEMS = (("MacBook Pro","Apple",2),("AC1200 Wireless Adapter","ALFA Network",4),("Jetson Nano Developer Kit","NVIDIA",3),("WRT1900AC Dual-Band Wi-Fi Router","Linksys",2),("RoboMaster EP","DJI",2))
INDEX_ITEM_NAME = 0
INDEX_USER_BORROW_RECORD = 0
FUNCTION_BORROW_ITEM = 0
working_directory = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
config = ConfigParser()

# you may implement other necessary functions here
# def checkWindows():
#     return (("win" in sys.platform.lower()) or ("windows" in sys.platform.lower()))

def display():
    print("Invnentory Management System")
    print(f"No. ")
    display_function_list = ("Borrow Item", "Return Item", "Display User Records", "Display All Records")
    for runtime in range(len(display_function_list)):
        print(f"{runtime:<3} | {display_function_list[runtime]}")
    return input(f"Please input your choice. (0-{len(display_function_list)}, Enter to return) : ")

# write a function remaining_quantity which accepts one parameter(tuple item)
def remaining_quantity(item):
    # complete your function here
    # this function should return the total quantity from the tuple item

    return item[3]

# write a function items_in_stock to display the main menu
def items_in_stock():
    # complete your function here
    # this function have no return value
    pass

# write a function items_borrowed which accepts one parameter(string borrower_name)
def items_borrowed(borrower_name):
    # complete your function here
    # this function should return the number of quantity of particular item borrowed by the borrower
    pass




def main():
    global user_list
    user_list = list()
    global user_borrow_record
    user_borrow_record = dict()
    config.read(working_directory + 'config.ini', "r")
    if (config.get("storage", "user") == "txt"):
        for user in open(working_directory + "/borrowers.txt", "r"):
            if not (user.startswith("# ") or (user == "\n")): user_list.append(user.rstrip("\n"))
    print("Welcome to Invnentory Management System.")
    while True:
        # display inventory management system menu and ask for user input

        input_function = display()

        # When user input 0 to borrow item
        if input_function == FUNCTION_BORROW_ITEM:
            # your logics for user selected borrow item function here
            pass


        # When user input 1 to return item
        elif input_function == FUNCTION_RETURN_ITEM:
            # your logics for user selected return item function here
            pass

        # When user input 2 to display a particular borrower's record
        elif input_function == DISPLAY_USER_RECORDS:
            # your logics for user selected display borrower's record here
            pass

        # When user input 3 to display all records
        elif input_function == DISPLAY_ALL_RECORDS:
            # your logics for user selected display all records here
            pass
