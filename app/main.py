import os
from .debug import dprint
from .display import Display as display

def items_borrow(borrower_name, item_no, item_quantity):
    user_no = int(user.get().name().get(str(borrower_name)))
    dprint("Loading items_borrow function")
    # ---Writing item data(txt) - Start---
    if config.storage.item == "txt":
        dprint("TXT mode")
        for borrowed in borrow.record():
            data = borrowed.split(", ")
            if (int(data[0]) == user_no) and (int(data[1]) == int(item_no)):
                dprint("replace mode")
                with open(ev.working_directory + "/data/borrowed.txt", "r+") as file:
                    file_date = file.read()
                    file_date = file_date.replace(f"{data[0]}, {data[1]}, {data[2]}",
                                                  f"{data[0]}, {data[1]}, {int(data[2]) + item_quantity}")
                    file.write(file_date)
                    file.close()
                    return True
        with open(ev.working_directory + "/data/borrowed.txt", "a") as file:
            dprint("writing mode")
            file.write(str(f"\n{user_no}, {item_no}, {item_quantity}"))
            file.close()
        return True
    # ---Writing item data(txt) - End---
    return False


def items_return(borrower_name, item_no, item_quantity):
    user_no = int(user.get().name().get(str(borrower_name)))
    dprint("Loading items_return function")
    # ---Writing item data(txt) - Start---
    if config.get("storage", "item") == "txt":
        dprint("TXT mode")
        for borrowed in borrow.record():
            data = borrowed.split(", ")
            if (int(data[0]) == user_no) and (int(data[1]) == int(item_no)):
                if (int(data[2]) - item_quantity) > 0:
                    dprint("replace mode")
                    with open(ev.working_directory + "/data/borrowed.txt", "r+") as file:
                        file_date = file.read()
                        file_date = file_date.replace(f"{data[0]}, {data[1]}, {data[2]}",
                                                      f"{data[0]}, {data[1]}, {int(data[2]) - item_quantity}")
                        file.write(file_date)
                        file.close()
                else:
                    dprint("remove mode")
                    with open(ev.working_directory + "/data/temp.txt", "a") as file_write, \
                            open(ev.working_directory + "/data/borrowed.txt", "r") as file_read:
                        for i in file_read:
                            if not i.strip("\n").startswith(f"{data[0]}, {data[1]}, {data[2]}"):
                                dprint(f"{i=}")
                                file_write.write(i)
                    os.replace(ev.working_directory + "/data/temp.txt", ev.working_directory + "/data/borrowed.txt")
                dprint("items_return function run successfully")
                return True
    # ---Writing item data(txt) - End---


def main():
    print("Welcome to Inventory Management System.")
    while True:
        # display inventory management system menu and ask for user input
        display().function()
        input_function = check.userinput(f"Please input your choice. (0-{len(ev.ITEMS.value) - 1}, Enter to return): ",
                                         "select_function",
                                         ev.function_list,
                                         "exit(0)")
        # When user input 0 to borrow item
        if input_function == ev.FUNCTION_BORROW_ITEM.value:
            # your logics for user selected borrow item function here
            print("")
            display().items()
            borrow_item = check.userinput(
                f"Please input the item no. to borrow (0 - {len(ev.ITEMS.value) - 1}, Enter to return): ",
                "borrow_item_no",
                "",
                "retry")
            borrow_quantity = check.userinput(f"Please input the quantity to borrow, Enter to return: ",
                                              "borrow_quantity",
                                              borrow_item,
                                              "retry")
            ask_borrow_user = check.userinput(f"Please input borrower's name, Enter to return: ",
                                              "username",
                                              "",
                                              "retry")
            items_borrow(ask_borrow_user, borrow_item, borrow_quantity)
            display().borrowed(ask_borrow_user)

        # When user input 1 to return item
        elif input_function == ev.FUNCTION_RETURN_ITEM.value:
            # your logics for user selected return item function here
            print("")
            borrow_user = check.userinput(f"Please input borrower's name, Enter to return: ",
                                          "username",
                                          "",
                                          "retry")
            dprint(f"calling display_borrowed\nask_borrow_user = {borrow_user}")
            display().borrowed(borrow_user)
            borrow_item = check.userinput(f"Please input the item no. to return Enter to return: ",
                                          "return_item_no",
                                          "",
                                          "retry")
            borrow_quantity = check.userinput(f"Please input the quantity to return, Enter to return: ",
                                              "return_quantity",
                                              (borrow_user, borrow_item),
                                              "retry")
            dprint(f"calling items_return\n"
                   f"ask_borrow_user = {borrow_user}\n"
                   f"ask_borrow_item = {borrow_item}\n"
                   f"ask_borrow_quantity = {borrow_quantity}")
            items_return(borrow_user, borrow_item, borrow_quantity)
            dprint(f"calling display_borrowed\nask_borrow_user = {borrow_user}")
            display().borrowed(borrow_user)

        # When user input 2 to display a particular borrower's record
        elif input_function == ev.DISPLAY_USER_RECORDS.value:
            # your logics for user selected display borrower's record here
            dprint(f"calling display_borrowed with following giving username")
            ask_borrow_user = check.userinput(f"Please input borrower's name, Enter to return: ",
                                              "username",
                                              "",
                                              "retry")
            display().borrowed(ask_borrow_user)

        # When user input 3 to display all records
        elif input_function == ev.DISPLAY_ALL_RECORDS.value:
            # your logics for user selected display all records here
            dprint(f"calling display_borrowed")
            display().borrowed()
