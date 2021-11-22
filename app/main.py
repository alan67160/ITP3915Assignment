# inport
import os
from enum import Enum
from .util import dprint
from .config import Config
from .environment_variable import Variable as ev


# you may implement other necessary functions here
class ask:
    class check_type(Enum):
        select_function = "select_function"
        username = "username"
        return_username = "return_username"
        borrow_item_no = "borrow_item_no"
        return_item_no = "return_item_no"
        borrow_quantity = "borrow_quantity"
        return_quantity = "return_quantity"

    def check(self, ask_msg, ask_type, arg, empty_result_action):
        while True:
            dprint("ask function - asking")
            result = input(ask_msg)
            dprint("ask function - checking empty")
            if result == "":
                print("The input can't be empty")
                if empty_result_action == "retry":
                    continue
                if not (empty_result_action == "ignore"):
                    exec(empty_result_action)
            dprint("ask function - checking user input")
            if ask_type == "select_function":
                try:
                    result = int(result)
                    if (result < 0) or (result > len(arg)):  # user input are less then 0 or more then the function list
                        print("Invalid input for choice")
                        continue
                except ValueError:  # user input are not integer
                    print("Invalid input for choice")
                    continue
                break
            if ask_type == "username":
                try:
                    is_a_user = False  # initializing the is_a_user variable
                    for no, username in user_list.items():  # Load user list
                        if username == result:  # Check the input have a match on user list or not
                            is_a_user = True  # if have a match set is_a_user to true
                            break  # stop the for loop
                    if not is_a_user:  # user input are a valid user on user list
                        print("Not a valid username.")  # print error to user
                        continue  # ask again
                except ValueError:  # user input are not string
                    print("Invalid value for quantity")  # print error to user
                    continue  # ask again
                break
            if ask_type == "return_username":
                try:
                    is_a_user = False
                    for no, username in user_list.items():
                        if username == result:
                            is_a_user = True
                            break
                    if not is_a_user:
                        print("Not a valid username.")
                        continue
                    if not items_borrowed(result):
                        print(f"{result} did not borrow any items")
                        continue
                except ValueError:
                    print("Invalid value for quantity")
                    continue
                break
            if ask_type == "borrow_item_no":
                try:
                    result = int(result)
                    if remaining_quantity(result) < 0:
                        print("The selected item is currently out of stock.")
                        continue
                    if (result < 0) or (len(ITEMS) < result):
                        print("you can't select a non-exist item")
                        continue
                except ValueError:
                    print("Invalid value for item no.")
                    continue
                break
            if ask_type == "return_item_no":
                try:
                    result = int(result)
                    if (result < 0) or ((len(ITEMS) - 1) < result):
                        print("you can't select a non-exist item")
                        continue
                    has_borrowed = False
                    for borrowed in get_borrowed_list():
                        if (borrowed[0] == arg) and (borrowed[1] == result):
                            has_borrowed = True
                    if has_borrowed:
                        print("you haven't borrowed this item before")
                except ValueError:
                    print("Invalid value for item no.")
                    continue
                break
            if ask_type == "borrow_quantity":
                try:
                    result = int(result)
                    if remaining_quantity(int(arg)) < result:
                        print("Your requested quantity is over our stock.")
                        continue
                    if result < 1:
                        print("Your can't borrow less then 1 item")
                        continue
                except ValueError:
                    print("Invalid value for quantity")
                    continue
                break
            if ask_type == "return_quantity":
                try:
                    result = int(result)
                    mq = 0
                    user_no = int(user_list_by_name.get(str(arg[0])))
                    for i in items_borrowed(int(user_no)):
                        if int(i[1]) == int(arg[1]):
                            mq += int(i[2])
                    dprint(mq)
                    if mq < result:
                        dprint("user want to donate item")
                        print("Your return quantity is over your borrow record.")
                        continue
                    if result > 1:
                        dprint("user want to return nothing or taking our stuff")
                        print("You can't return less then 1 item.")
                        continue
                except ValueError:
                    print("Invalid value for quantity")
                    continue
                break
        return result


def display():
    print("Inventory Management System Menu:")
    print(f"No. | Function")
    for runtime in range(len(ev.function_list.value)):
        print(f"{runtime:<3} | {ev.function_list.value[runtime]}")


def display_borrowed(user_name=""):
    try:
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
    except IndexError:
        pass


# a function remaining_quantity which accepts one parameter(UniqueItemNo)
def remaining_quantity(item_no):
    dprint("remaining_quantity function")
    dprint(f"base_quantity = {tuple(ITEMS[item_no])[2]}")
    dprint(f"borrowed_quantity = {get_borrowed_quantity(item_no)}")
    dprint(f"remaining_quantity = {int(tuple(ITEMS[item_no])[2]) - int(get_borrowed_quantity(item_no))}")
    return int(tuple(ITEMS[item_no])[2]) - int(get_borrowed_quantity(item_no))


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
            if int(item[1]) == item_no:
                borrowed_quantity += int(item[2])
    return borrowed_quantity


def get_borrowed_list():
    dprint("Loading borrow record")
    # ---Loading item data(txt) - Start---
    if Config.borrowed == "txt":
        with open(ev.working_directory.value + "/data/borrowed.txt", "r") as file:
            dprint("TXT mode")
            raw_borrowed = str()
            for read in file:
                if not (read.startswith("# ") or (read == "\n")):
                    raw_borrowed += read
            if Config.debug:
                dprint(f"Item No. | Item Name                                  | borrower   | Qty. borrowed")
                for record in tuple(filter(None, raw_borrowed.split("\n"))):
                    data = record.split(", ")
                    dprint(f"data[1] = {data}")
                    dprint(f"ITEMS[data[1]][0] = {ITEMS[int(data[1])][0]}")
                    dprint(f"ITEMS[data[1]][1] = {ITEMS[int(data[1])][1]}")
                    name = f"{ITEMS[int(data[1])][0]} - {ITEMS[int(data[1])][1]}"
                    dprint(f"{data[1]:>7}. | {name:<42} | {user_list[int(data[0])]:<10} | {data[2]:>13}")
            raw_borrowed = tuple(filter(None, raw_borrowed.split("\n")))
            dprint(f"raw_borrowed = {raw_borrowed}")
            return raw_borrowed
    # ---Loading item data(txt) - End---


# write a function items_in_stock to display the main menu
def items_in_stock():
    # complete your function here
    # this function have no return value
    print(f"Item No. | Item Name                                  | Qty. Left")
    dprint("items_in_stock function")
    dprint(f"ITEMS = {ITEMS}")
    for runtime in range(len(ITEMS)):
        item_name = str(ITEMS[runtime][0] + " - " + ITEMS[runtime][1])
        print(f"{runtime:>7}. | {item_name:<42} | {remaining_quantity(runtime):>9}")


# write a function items_borrowed which accepts one parameter(UniqueUserNo)
def items_borrowed(borrower_no):
    results = list()
    for i in get_borrowed_list():
        data = i.split(", ")
        if int(data[0]) == borrower_no:
            results.append(data)
    return results


def items_borrow(borrower_name, item_no, item_quantity):
    user_no = int(user_list_by_name.get(str(borrower_name)))
    dprint("Loading items_borrow function")
    if Config.borrow_limit == 0:
        print("I''m sorry, but borrowing functions are currently disabled by the administrator.\n"
              "Please contact the server administrators if you believe that this is in error.")
        return False
    if Config.borrow_limit > 1:
        borrowed_quantity = 0
        for i in items_borrowed(user_no):
            borrowed_quantity += int(i[2])
        if (borrowed_quantity + item_quantity) > Config.borrow_limit:
            print("I''m sorry, but you have reached the borrow maximum.\n"
                  "Please contact the system administrators if you believe that this is in error.")
        return False
    # ---Writing item data(txt) - Start---
    if Config.item == "txt":
        dprint("TXT mode")
        for borrowed in get_borrowed_list():
            data = borrowed.split(", ")
            if (int(data[0]) == user_no) and (int(data[1]) == int(item_no)):
                dprint("replace mode")
                with open(ev.working_directory.value + "/data/borrowed.txt", "r+") as file:
                    file_date = file.read()
                    file_date = file_date.replace(f"{data[0]}, {data[1]}, {data[2]}",
                                                  f"{data[0]}, {data[1]}, {int(data[2]) + item_quantity}")
                    file.write(file_date)
                    file.close()
                    return True
        with open(ev.working_directory.value + "/data/borrowed.txt", "a") as file:
            dprint("writing mode")
            file = open(ev.working_directory.value + "/data/borrowed.txt", "a")
            file.write(str(f"\n{user_no}, {item_no}, {item_quantity}"))
            file.close()
        return True
    # ---Writing item data(txt) - End---
    return False


def items_return(borrower_name, item_no, item_quantity):
    user_no = int(user_list_by_name.get(str(borrower_name)))
    dprint("Loading items_return function")
    if Config.borrow_limit == 0:
        print("I''m sorry, but borrowing functions are currently disabled by the administrator.\n"
              "Please contact the server administrators if you believe that this is in error.")
        return False
    # ---Writing item data(txt) - Start---
    if Config.item == "txt":
        dprint("TXT mode")
        for borrowed in get_borrowed_list():
            data = borrowed.split(", ")
            if (int(data[ev.INDEX_USER_NO.value]) == user_no) and (int(data[ev.INDEX_ITEM_NO.value]) == int(item_no)):
                if (int(data[2]) - item_quantity) > 0:
                    dprint("replace mode")
                    with open(ev.working_directory.value + "/data/borrowed.txt", "r") as file_read, \
                            open(ev.working_directory.value + "/data/borrowed.txt", "w") as file_write:
                        file_date = file_read.read()
                        file_date = file_date.replace(f"{data[0]}, {data[1]}, {data[2]}",
                                                      f"{data[0]}, {data[1]}, {int(data[2]) - item_quantity}")
                        file_write.write(file_date)
                        file_write.close()
                else:
                    dprint("remove mode")
                    with open(ev.working_directory.value + "/data/temp.txt", "a") as file_write:
                        for i in open(ev.working_directory.value + "/data/borrowed.txt", "r"):
                            if not i.strip("\n").startswith(f"{data[0]}, {data[1]}, {data[2]}"):
                                dprint(f"data: {i}")
                                file_write.write(i)
                    os.replace(ev.working_directory.value + "/data/temp.txt",
                               ev.working_directory.value + "/data/borrowed.txt")
                dprint("items_return function run successfully")
                return True
    # ---Writing item data(txt) - End---


def main():
    dprint("System initializing...")
    # Assign global variables
    dprint("initializing global variables...")
    global user_list
    global user_list_by_name
    global user_borrow_record
    global ITEMS
    dprint("Global variables loaded!", "ok")
    # Assign variables
    dprint("initializing variables...")
    user_list = dict()
    user_list_by_name = dict()
    user_borrow_record = dict()
    ITEMS = tuple()
    dprint("Variables loaded!", "ok")
    dprint("initializing user list...")
    if Config.user == "txt":
        dprint("TXT mode")
        sub_user_list = list()
        dprint(f"Loading {ev.working_directory.value}/data/borrowers.txt")
        for user in open(ev.working_directory.value + "/data/borrowers.txt", "r"):
            if not (user.startswith("# ") or (user == "\n")):
                sub_user_list.append(user.rstrip("\n").split(", "))
        dprint(f"No. | Username", "data")
        for runtime in range(len(sub_user_list)):
            dprint(f"{runtime:<3} | {str(sub_user_list[runtime][0]).lower()}", "data")
            user_list[runtime] = str(sub_user_list[runtime][0]).lower()
            user_list_by_name[str(sub_user_list[runtime][0]).lower()] = runtime
        dprint("User list Loaded!", "ok")
    try:
        user_list
    except NameError:
        dprint("\033[91m[WARN] An unexpected error occurred while trying to initialize the user list...")
    dprint("setting up base item list...")
    if Config.item == "txt":
        dprint("TXT mode")
        raw_items = str()
        sub_items = tuple()
        ITEMS = list()
        dprint(f"Loading {ev.working_directory.value}/data/items.txt")
        with open(ev.working_directory.value + "/data/items.txt", "r") as file:
            for read in file:
                if not (read.startswith("# ") or (read == "\n")):
                    raw_items += read
            raw_items = raw_items.split("\n")
            dprint(f"ItemName                                   | ItemBrand       | ItemQuantity")
            for runtime in range(len(raw_items)):
                sub_items += tuple(raw_items[runtime].split(", "))
                if len(sub_items) == 3:
                    dprint(f"{sub_items[0]:<42} | {sub_items[1]:<15} | {sub_items[2]}")
                    ITEMS.append(tuple(sub_items))
                    sub_items = ()
            ITEMS = tuple(ITEMS)
        dprint("Base item list Loaded!", "ok")
    dprint("System Started", "ok")
    print("Welcome to Inventory Management System.")
    while True:
        # display inventory management system menu and ask for user input
        display()
        input_function = ask().check(
            f"Please input your choice. (0-{len(ev.function_list.value) - 1}, Enter to return): ",
            ask.check_type.select_function.value,
            ev.function_list.value,
            "exit(0)")
        # When user input 0 to borrow item
        if input_function == ev.FUNCTION_BORROW_ITEM.value:
            # your logics for user selected borrow item function here
            print("")
            items_in_stock()
            borrow_item = ask().check(f"Please input the item no. to borrow (0 - {len(ITEMS) - 1}, Enter to return): ",
                                      ask.check_type.borrow_item_no.value,
                                      "",
                                      "retry")
            borrow_quantity = ask().check(f"Please input the quantity to borrow, Enter to return: ",
                                          ask.check_type.borrow_quantity.value,
                                          borrow_item,
                                          "retry")
            borrow_user = ask().check(f"Please input borrower's name, Enter to return: ",
                                      ask.check_type.username.value,
                                      "",
                                      "retry")
            if items_borrow(borrow_user, borrow_item, borrow_quantity):
                display_borrowed(borrow_user)
                print(f"{borrow_user} borrowed {borrow_quantity} {ITEMS[borrow_item][0]} successfully.")

        # When user input 1 to return item
        elif input_function == ev.FUNCTION_RETURN_ITEM.value:
            # your logics for user selected return item function here
            print("")
            borrow_user = ask().check(f"Please input borrower's name, Enter to return: ",
                                      ask.check_type.return_username.value,
                                      "",
                                      "retry")
            dprint(f"calling display_borrowed\nask_borrow_user = {borrow_user}")
            display_borrowed(borrow_user)
            borrow_item = ask().check(f"Please input the item no. to return Enter to return: ",
                                      ask.check_type.return_item_no.value,
                                      borrow_user,
                                      "retry")
            borrow_quantity = ask().check(f"Please input the quantity to return, Enter to return: ",
                                          ask.check_type.return_quantity.value,
                                          (borrow_user, borrow_item),
                                          "retry")
            dprint(f"calling items_return\n"
                   f"ask_borrow_user = {borrow_user}\n"
                   f"ask_borrow_item = {borrow_item}\n"
                   f"ask_borrow_quantity = {borrow_quantity}")
            if items_return(borrow_user, borrow_item, borrow_quantity):
                dprint(f"calling display_borrowed\nask_borrow_user = {borrow_user}")
                display_borrowed(borrow_user)
                print(f"{borrow_user} returned {borrow_quantity} {ITEMS[borrow_item][0]} successfully.")

        # When user input 2 to display a particular borrower's record
        elif input_function == ev.DISPLAY_USER_RECORDS.value:
            # your logics for user selected display borrower's record here
            dprint(f"calling display_borrowed with following giving username")
            ask_borrow_user = ask().check(f"Please input borrower's name, Enter to return: ",
                                          ask.check_type.username.value,
                                          "",
                                          "retry")
            display_borrowed(ask_borrow_user)
        # When user input 3 to display all records
        elif input_function == ev.DISPLAY_ALL_RECORDS.value:
            # your logics for user selected display all records here
            dprint(f"calling display_borrowed")
            display_borrowed()
