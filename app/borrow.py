from .debug import dprint
from .environment_variable import Variable as ve
from .config import Config as config


class borrow:
    # a function remaining_quantity which accepts two parameter(UniqueItemNo, UniqueUserNo)
    # if only one parameter were giving the, It would mean getting borrowed quantity for all user
    def quantity(self, item_no, *user_no):
        borrowed_quantity = int(0)
        for borrowed_item in borrow().record():
            item = borrowed_item.split(", ")
            if user_no in locals():
                if (int(item[1]) == item_no) and (int(item[0]) == user_no):
                    borrowed_quantity += int(item[2])
            else:
                if int(item[1]) == item_no:
                    borrowed_quantity += int(item[2])
        return borrowed_quantity


    def record(self):
        dprint("Loading borrow record")
        # ---Loading item data(txt) - Start---
        if config.storage.borrowed.value == "txt":
            with open(str(ve.working_directory) + "/data/borrowed.txt", "r") as file:
                dprint("TXT mode")
                raw_borrowed = str()
                for read in file:
                    if not (read.startswith("# ") or (read == "\n")):
                        raw_borrowed += read
                if config.debug:
                    dprint(f"Item No. | Item Name                                  | borrower   | Qty. borrowed")
                    for record in tuple(filter(None, raw_borrowed.split("\n"))):
                        data = record.split(", ")
                        dprint(f"{data=}")
                        dprint(f"{ITEMS[int(data[1])][0]=}")
                        dprint(f"{ITEMS[int(data[1])][1]=}")
                        name = f"{ITEMS[int(data[1])][0]} - {ITEMS[int(data[1])][1]}"
                        dprint(f"{data[1]:>7}. | {name:<42} | {user_list[int(data[0])]:<10} | {data[2]:>13}")
                raw_borrowed = tuple(filter(None, raw_borrowed.split("\n")))
                dprint(f"{raw_borrowed=}")
                return raw_borrowed
        # ---Loading item data(txt) - End---

    def borrowed(self, borrower_no):
        results = list()
        for i in borrow().record():
            data = i.split(", ")
            if int(data[0]) == borrower_no:
                results.append(data)
        return results

