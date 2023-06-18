import pytest

import date_util

# Data for test_get_nbr_days_in_month() unit test
@pytest.mark.parametrize(
    "month_str, year_int, expected_output, expected_exception",
    [   # Positive tests
       ("January", 2023, 31, False),
        ("FEBRUARY", 2023, 28, False),
        ("february", 2020, 29, False),
        ("March", 2023, 31, False),
        ("April", 2023, 30, False),
        ("May", 2019, 31, False),
        ("June", 2000, 30, False),
        ("July", 2025, 31, False),
        ("August", 2026, 31, False),
        ("September", 2001, 30, False),
        ("octOBER", 2010, 31, False),
        ("NOVEMBER", 2011, 30, False),
        ("December", 2016, 31, False),
        ("Jan", 2023, 31, False),
        ("FEB", 2023, 28, False),
        ("Mar", 2023, 31, False),
        ("Apr", 2023, 30, False),
        ("May", 2019, 31, False),
        ("Jun", 2000, 30, False),
        ("Jul", 2025, 31, False),
        ("Aug", 2026, 31, False),
        ("Sep", 2001, 30, False),
        ("oct", 2010, 31, False),
        ("NOV", 2011, 30, False),
        ("Dec", 2016, 31, False),
        # Negative tests
        ("invalid-month-name", 2023, -1, True)
    ]
)
def test_get_nbr_days_in_month(month_str, year_int, expected_output, expected_exception):
    act_output = None
    exception_occurred = False
    try:
        act_output = date_util.get_nbr_days_in_month(month_str, year_int)
    except:
        exception_occurred = True

    assert exception_occurred == expected_exception
    if not expected_exception:
        assert act_output == expected_output


def test_get_nbr_days_in_month_sandbox():
    # Setup
    # Act
    nbr_days_in_month = date_util.get_nbr_days_in_month("January", 2023)
    # Assert
    assert nbr_days_in_month == 31
    # Cleanup

