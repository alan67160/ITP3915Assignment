from .borrow import borrow
from .user import main as user
from .util import main as user
from .debug import dprint
from .items import Items
from .environment_variable import Variable as ev
ITEMS = Items().get()

class Display:
    def function(self) -> None:
        print("Inventory Management System Menu:")
        print(f"No. | Function")
        for runtime in range(len(ev.function_list.value)):
            print(f"{runtime:<3} | {ev.function_list[runtime]}")

    def borrowed(self, *borrower) -> None:
        try:
            if not borrower == "":
                user_no = int(user().name().get(str(user)))
                print()
                print(f"Item No. | Item Name                                  | Qty. borrowed")
                for data in borrow().record():
                    item_data = data.split(", ")
                    item_name = str(ITEMS[int(item_data[1])][0] + " - " + ITEMS[int(item_data[1])][1])
                    if user_no == int(item_data[0]):
                        print(f"{item_data[1]:>7}. | {item_name:<42} | {item_data[2]:>13}")
                print()
            else:
                print()
                print(f"Item No. | Item Name                                  | borrower   | Qty. borrowed")
                for data in borrow().record():
                    item_data = data.split(", ")
                    item_name = str(ITEMS[int(item_data[1])][0] + " - " + [int(item_data[1])][1])
                    print(f"{item_data[1]:>7}. | {item_name:<42} | {user().name()[int(item_data[0])]:<10} | {item_data[2]:>13}")
                print()
        except IndexError:
            pass

    def items(self) -> None:
        print(f"Item No. | Item Name                                  | Qty. Left")
        dprint("items_in_stock function")
        dprint(f"{ITEMS=}")
        for runtime in range(len(ITEMS)):
            item_name = str(ITEMS[runtime][0] + " - " + ITEMS[runtime][1])
            print(f"{runtime:>7}. | {item_name:<42} | {util().remaining_quantity(runtime):>9}")

