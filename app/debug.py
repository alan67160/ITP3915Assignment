from .config import Config as config

def dprint(msg, debug_type="info"):  # creating a function call "dprint", and it will accept 2 parameter
    # msg is required, the message that I will print
    # debug_type is optional, the message type for set the message color
    if config.debug:  # checking if the debug is on
        color = ""
        debug_type = str(debug_type).lower()  # set the debug_type to lower case to reduce case unwatch issues
        if debug_type == "info":  # checking if the debug_type is "info" or not
            color = "\033[34m"  # set color red
        if debug_type == "data":  # checking if the debug_type is "data" or not
            color = "\033[94m"  # set color red
        elif debug_type == "ok":  # checking if the debug_type is "ok" or not
            color = "\033[92m"  # set color green
        elif debug_type == "warn":  # checking if the debug_type is "warn" or not
            color = "\033[93m"  # set color yellow
        elif debug_type == "fail":  # checking if the debug_type is "fail" or not
            color = "\033[91m"  # set color red
        print(f"\033[92m[金寶綠水]\033[0m {color}{msg}\033[0m")  # print debug message with prefix