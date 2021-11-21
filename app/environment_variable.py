import os
from enum import Enum


class Variable(Enum):
    working_directory = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
    function_list = ("Borrow Item", "Return Item", "Display User Records", "Display All Records")
    FUNCTION_BORROW_ITEM = 0
    FUNCTION_RETURN_ITEM = 1
    DISPLAY_USER_RECORDS = 2
    DISPLAY_ALL_RECORDS = 3
    # ITEMS = Items().get()
    INDEX_ITEMS_NAME = 0
    INDEX_ITEMS_BRAND = 1
    INDEX_ITEMS_QUANTITY = 2
