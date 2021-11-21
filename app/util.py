from .borrow import borrow
from .debug import dprint
from .environment_variable import Variable as ev


class main:
    def remaining_quantity(item_no):
        dprint("remaining_quantity function")
        dprint(f"base_quantity={tuple(ev.ITEMS[item_no])[2]}")
        dprint(f"borrowed_quantity={borrow().quantity(item_no)}")
        quantity = (int(tuple(ev.ITEMS[item_no])[ev.INDEX_ITEMS_QUANTITY.value]) - int(borrow().quantity(item_no)))
        dprint(f"remaining_quantity={quantity}")
        return quantity

