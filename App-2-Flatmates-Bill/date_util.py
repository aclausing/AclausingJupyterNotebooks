# Limitation: only works for years 1901 to 2099
def get_nbr_days_in_month(month_str: str, year_int: int) -> int:
    """
    Input parameter month_str is type str, e.g., "January" or "December" or "jan" or "DEC", case-insensitive
    Input parameter year_int is type int, e.g., 2023
    :return number of days in month
    """

    # Validate input parameters
    # Assert statement documentation is here: https://www.programiz.com/python-programming/assert-statement#:~:text=Python%20has%20built%2Din%20assert,program%20and%20gives%20an%20AssertionError%20.
    assert isinstance(month_str,
                      str), "get_nbr_days_in_month: month_str is type " + month_str.__class__.__name__ + ", must be type str or subclass"
    assert isinstance(year_int,
                      int), "get_nbr_days_in_month: year_int is type " + year_int.__class__.__name__ + ", must be type int or subclass"

    # nbr_days_in_month = 31
    month_str3 = month_str[0:3].lower()   # 1st 3 characters only
    if month_str3 in ("apr", "jun", "sep", "nov"):  # 30 day month April, June, September, November
        nbr_days_in_month = 30
    elif month_str3 == "feb":  # February is 28 or 29 day month
        nbr_days_in_month = 28
        if (year_int % 4) == 0:
            nbr_days_in_month = 29
    elif month_str3 in ("jan", "mar", "may", "jul", "aug", "oct", "dec"):
        nbr_days_in_month = 31
    else:
        raise Exception(month_str + " is not a valid month name")
    return nbr_days_in_month

