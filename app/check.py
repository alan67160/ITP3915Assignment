from debug import dprint
import user
import util
from environment_variable import Variable as ev
import borrow

def userinput(ask_msg, ask_type, arg, empty_result_action):
    while True:
        dprint("ask function - asking")
        result = input(ask_msg)
        if empty_result_action == "retry":
            empty_result_action = "ask(ask_msg, ask_type, arg, empty_result_action)"
        dprint("ask function - check empty")
        if (result == "") and not (empty_result_action == "ignore"):
            print("The input can't be empty")
            exec(empty_result_action)
            break
        dprint("ask function - check user input")
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
                for no, username in user.get().name().items():  # Load user list
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
        if ask_type == "borrow_item_no":
            try:
                result = int(result)
                if util.remaining_quantity(result) < 0:
                    print("The selected item is currently out of stock.")
                    continue
                if (result < 0) or (len(ev.ITEMS.value) < result):
                    print("you can't select a non-exist item")
                    continue
            except ValueError:
                print("Invalid value for item no.")
                continue
            break
        if ask_type == "return_item_no":
            try:
                result = int(result)
                if (result < 0) or (result > len(ev.ITEMS.value)):  # user input are less then 0 or more then the item type list
                    print("you can't select a non-exist item")
                    continue
            except ValueError:
                print("Invalid value for item no.")
                continue
            break
        if ask_type == "borrow_quantity":
            try:
                result = int(result)
                if util.remaining_quantity(int(arg)) < result:
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
                user_no = int(user.get().name().get(str(arg[0])))
                for i in borrow.borrowed(int(user_no)):
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