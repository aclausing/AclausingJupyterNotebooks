from decimal import Decimal


def get_decimal_from_console(prompt: str) -> Decimal:
    retval = None
    while retval is None:
        retval_str = input(prompt)
        try:
            retval = Decimal(retval_str)
        except:
            print(retval_str + " is not a dollar amount. Please try again.")
    return retval


def get_float_from_console(prompt: str) -> float:
    retval = None
    while retval is None:
        retval_str = input(prompt)
        try:
            retval = float(retval_str)
        except:
            print(retval_str + " is not a float. Please try again.")
    return retval


def get_int_from_console(prompt: str) -> int:
    """
    Prints prompt, gets value from user, converts value to integer.
    Does not return until valid integer is input by user.
    """
    retval = None
    while retval is None:
        retval_str = input(prompt)
        try:
            retval = int(retval_str)
        except:
            print(retval_str + " is not an integer. Please try again.")
    return retval
