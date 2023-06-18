# import logging
import pytest

from bill import Bill
from flatmate import Flatmate


class TestBill:

    def test_calc_shares_sandbox1(self):
        """For debugging parameterized test case which is failing"""

        # Setup
        billdata = Bill(12.25, 30, "September 2022")
        flatmate_dict = dict()
        flatmate1 = Flatmate("Alexis", 30)
        flatmate_dict[flatmate1.name] = flatmate1
        flatmate2 = Flatmate("Charlie", 30)
        flatmate_dict[flatmate2.name] = flatmate2
        # Act
        billdata.calc_shares(flatmate_dict)
        print(flatmate1.name, billdata.shares[flatmate1.name])
        print(flatmate2.name, billdata.shares[flatmate2.name])
        # Assert
        assert billdata.shares[flatmate1.name] == 6.12
        assert billdata.shares[flatmate2.name] == 6.13

    @pytest.mark.parametrize(
        "bill_data, flatmates_data, exp_shares",
        [  # test case#0: split evenly, one flatmate pays a penny more
            (
                    (12.25, 30, "September 2022"),
                    (("Alexis", 30), ("Charlie", 30)),
                    {"Alexis": 6.12, "Charlie": 6.13}
            ),
            # test case#1: one flatmate was away half the month
            (
                    (120.00, 30, "September 2022"),
                    (("Alexis", 30), ("Charlie", 15)),
                    {"Alexis": 80.00, "Charlie": 40.00}
            ),
            # test case#2: bill amount is $0.01
            (
                    (0.01, 30, "April 2022"),
                    (("Alexis", 30), ("Charlie", 30)),
                    {"Alexis": 0.01, "Charlie": 0.00}
            ),
            # test case#3: this failed during exploratory testing
            (
                    (112.45, 30, "September 2022"),
                    (("Alexis", 28), ("Charlie", 20)),
                    {"Alexis": 65.60, "Charlie": 46.85}
            ),
            # test case#4: 3 flatmates, none was away during the billing period
            (
                    (18.02, 30, "September 2022"),
                    (("Alexis", 30), ("Charlie", 30), ("Samson", 30)),
                    {"Alexis": 6.01, "Charlie": 6.01, "Samson": 6.00}
            ),
            # test case#5: 3 flatmates, two were away part of the entire billing period
            (
                    (18.02, 30, "September 2022"),
                    (("Alexis", 10), ("Charlie", 20), ("Samson", 30)),
                    {"Alexis": 3.00, "Charlie": 6.01, "Samson": 9.01}
            ),
            # test case#6: 3 flatmates, all were away during the entire billing period
            (
                    (18.02, 30, "September 2022"),
                    (("Alexis", 0), ("Charlie", 0), ("Samson", 0)),
                    {"Alexis": 6.01, "Charlie": 6.01, "Samson": 6.00}
            ),
        ]
    )
    def test_calc_shares(self, bill_data, flatmates_data, exp_shares):
        # Setup
        # LOGGER = logging.getLogger(__name__)
        bill = Bill(bill_data[0], bill_data[1], bill_data[2])
        flatmate_dict = dict()
        for flatmate_data in flatmates_data:
            flatmate = Flatmate(flatmate_data[0], flatmate_data[1])
            flatmate_dict[flatmate.name] = flatmate

        # Act
        bill.calc_shares(flatmate_dict)

        # Assert
        for flatmate_name in exp_shares.keys():
            assert bill.shares[flatmate_name] == exp_shares[flatmate_name]

    def test_calc_shares_sandbox2(self):
        # Setup
        billdata = Bill(120.00, 30, "September 2022")
        flatmate_dict = dict()
        flatmate1 = Flatmate("Alexis", 30)
        flatmate_dict[flatmate1.name] = flatmate1
        flatmate2 = Flatmate("Charlie", 15)
        flatmate_dict[flatmate2.name] = flatmate2
        # Act
        billdata.calc_shares(flatmate_dict)
        print(flatmate1.name, billdata.shares[flatmate1.name])
        print(flatmate2.name, billdata.shares[flatmate2.name])
        # Assert
        assert billdata.shares[flatmate1.name] == 80.00
        assert billdata.shares[flatmate2.name] == 40.00

    def test_calc_shares3(self):
        """bill amount is $0.01"""
        # Setup
        billdata = Bill(0.01, 30, "September 2022")
        flatmate_dict = dict()
        flatmate1 = Flatmate("Alexis", 30)
        flatmate_dict[flatmate1.name] = flatmate1
        flatmate2 = Flatmate("Charlie", 30)
        flatmate_dict[flatmate2.name] = flatmate2
        # Act
        billdata.calc_shares(flatmate_dict)
        print(flatmate1.name, billdata.shares[flatmate1.name])
        print(flatmate2.name, billdata.shares[flatmate2.name])
        # Assert
        assert billdata.shares[flatmate1.name] == 0.01
        assert billdata.shares[flatmate2.name] == 0.00

    def test_calc_shares4(self):
        # Setup
        billdata = Bill(18.02, 30, "September 2022")
        flatmate_dict = dict()
        flatmate1 = Flatmate("Alexis", 30)
        flatmate_dict[flatmate1.name] = flatmate1
        flatmate2 = Flatmate("Charlie", 30)
        flatmate_dict[flatmate2.name] = flatmate2
        flatmate3 = Flatmate("Samson", 30)
        flatmate_dict[flatmate3.name] = flatmate3
        # Act
        billdata.calc_shares(flatmate_dict)
        print(flatmate1.name, billdata.shares[flatmate1.name])
        print(flatmate2.name, billdata.shares[flatmate2.name])
        print(flatmate3.name, billdata.shares[flatmate3.name])
        # Assert
        assert billdata.shares[flatmate1.name] == 6.01
        assert billdata.shares[flatmate2.name] == 6.01
        assert billdata.shares[flatmate3.name] == 6.00
