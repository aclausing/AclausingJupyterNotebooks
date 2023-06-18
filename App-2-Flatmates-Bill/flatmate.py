from input_util import get_int_from_console


class Flatmate:
    """Name of flatmate and how many days he was living in flat during billing period"""

    def __init__(self, name_value: str, nbr_days_in_flat_value: int):
        self.name = name_value
        self.nbr_days_in_flat = nbr_days_in_flat_value

    def deepcopy(self) -> "Flatmate":
        """Returns deep copy of this instance"""

        retval = Flatmate(self.name, self.nbr_days_in_flat)
        return retval

    @classmethod
    def input_flatmate(cls, name_prompt: str) -> "Flatmate":
        """Creates new Flatmate object and populates from console inputs"""
        flatmate_name = input(name_prompt)
        flatmate_nbr_days = get_int_from_console(
            "How many days did " + flatmate_name + " stay in the house during the bill period? ")
        if flatmate_nbr_days < 0:
            flatmate_nbr_days = 0
        mate = Flatmate(flatmate_name, flatmate_nbr_days)
        return mate
