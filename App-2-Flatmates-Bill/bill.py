from date_util import get_nbr_days_in_month
from input_util import get_float_from_console
from flatmate import Flatmate


class Bill:
    """Bill information"""

    def __init__(self, amount_value: float, period_value: int, bill_period_str_value: str):
        """

        :param amount_value:
        :param period_value: number of days in month
        :param bill_period_str_value: month+year string, e.g., "December 2022"
        """
        self.amount = amount_value
        self.bill_period_days = period_value
        self.bill_period_str = bill_period_str_value
        self.shares = dict()  # key is flatmate name (str), value is dollar amount owed (float)

    def calc_shares(self, flatmates: dict[str, Flatmate]) -> None:
        """
        Calculates share of bill for each flatmate
        flatmates: dict key is flatmate name, value is Flatmate object
        """

        nbr_flatmates = len(flatmates.keys())

        # Deep copy the flatmates dict, because we may be changing nbr days in flat for calculation purposes
        flatmates_dict2 = dict()
        person_days_in_flat = 0
        for flatmate in flatmates.values():
            flatmates_dict2[flatmate.name] = flatmate.deepcopy()
            person_days_in_flat = person_days_in_flat + flatmate.nbr_days_in_flat

        # If nobody was in flat during entire billing period, everyone will split the bill equally
        if person_days_in_flat == 0:
            # fix it so the calculation doesn't blow up
            person_days_in_flat = len(flatmates_dict2.keys())
            for flatmate in flatmates_dict2.values():
                flatmate.nbr_days_in_flat = 1

        # Calculate shares
        total_shares = 0.00
        idx = 0
        for flatmate in flatmates_dict2.values():
            share_amount = self.amount * flatmate.nbr_days_in_flat / person_days_in_flat
            share_amount = round(share_amount, 2)  # round to nearest cent
            total_shares = total_shares + share_amount
            idx = idx + 1
            if idx == nbr_flatmates:  # if all flatmates have had shares calculated
                # Tweak shares if necessary, so the total of all shares equals the bill amount
                total_shares = round(total_shares, 2)
                if total_shares < self.amount:
                    share_amount = share_amount + 0.01
                    total_shares = total_shares + 0.01
                elif total_shares > self.amount:
                    share_amount = share_amount - 0.01
                    total_shares = total_shares - 0.01
            self.shares[flatmate.name] = round(share_amount, 2)

    @classmethod
    def input_bill(cls) -> "Bill":
        """
        Creates new Bill object and populates from console inputs
        """
        total_bill = 0.0
        while total_bill <= 0.0:
            total_bill = get_float_from_console("Enter the bill amount: ")
            if total_bill <= 0.0:
                print("Bill amount must be a positive number. Please try again.")

        bill_period_days = None
        while bill_period_days is None:
            bill_period_str = input("What is the bill period, e.g., December 2020: ")
            bill_period_tuple = bill_period_str.rpartition(" ")
            try:
                bill_period_days = get_nbr_days_in_month(bill_period_tuple[0], int(bill_period_tuple[2]))
            except:
                print(bill_period_str + " is not a valid month and year. Please try again.")

        retval = Bill(total_bill, bill_period_days, bill_period_str)
        return retval
