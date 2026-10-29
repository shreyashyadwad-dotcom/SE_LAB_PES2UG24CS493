import pytest
from bike_share_rental import ride_cost, dock_status, can_unlock


# ride_cost tests

def test_standard_ride():
    assert ride_cost("standard", 45, False, False) == 40

def test_electric_ride():
    assert ride_cost("electric", 30, False, False) == 35

def test_cargo_ride():
    assert ride_cost("cargo", 30, False, False) == 50

def test_subscriber_ride():
    assert ride_cost("standard", 60, True, False) == 20

def test_peak_ride():
    assert ride_cost("standard", 30, False, True) == 35

def test_long_ride():
    assert ride_cost("standard", 210, False, False) == 240

def test_invalid_bike_type():
    with pytest.raises(ValueError):
        ride_cost("mountain", 30, False, False)

def test_zero_duration():
    with pytest.raises(ValueError):
        ride_cost("standard", 0, False, False)

def test_negative_duration():
    with pytest.raises(ValueError):
        ride_cost("standard", -10, False, False)


# dock_status tests

def test_empty_dock():
    assert dock_status(0, 10) == "empty"

def test_full_dock():
    assert dock_status(10, 10) == "full"

def test_few_bikes():
    assert dock_status(2, 10) == "few bikes"

def test_few_slots():
    assert dock_status(8, 10) == "few slots"

def test_available_dock():
    assert dock_status(5, 10) == "available"

def test_invalid_capacity():
    with pytest.raises(ValueError):
        dock_status(0, 0)

def test_negative_bikes():
    with pytest.raises(ValueError):
        dock_status(-1, 10)

def test_excess_bikes():
    with pytest.raises(ValueError):
        dock_status(11, 10)


# can_unlock tests

def test_active_ride():
    assert can_unlock(200, True, 25) is False

def test_age_below_16():
    assert can_unlock(200, False, 15) is False

def test_age_16_sufficient_balance():
    assert can_unlock(100, False, 16) is True

def test_age_16_low_balance():
    assert can_unlock(99, False, 16) is False

def test_adult_sufficient_balance():
    assert can_unlock(50, False, 18) is True

def test_adult_low_balance():
    assert can_unlock(49, False, 18) is False