import pytest
from bike_share_rental import ride_cost, dock_status, can_unlock


# ride_cost: bike type branches

def test_all_bike_types():
    assert ride_cost("standard", 30, False, False) == 20
    assert ride_cost("electric", 30, False, False) == 35
    assert ride_cost("cargo", 30, False, False) == 50


def test_invalid_bike_type():
    with pytest.raises(ValueError):
        ride_cost("unknown", 30, False, False)


# ride_cost: duration branches

def test_invalid_durations():
    with pytest.raises(ValueError):
        ride_cost("standard", 0, False, False)

    with pytest.raises(ValueError):
        ride_cost("standard", -1, False, False)


def test_duration_boundaries():
    assert ride_cost("standard", 1, False, False) == 20
    assert ride_cost("standard", 30, False, False) == 20
    assert ride_cost("standard", 31, False, False) == 40


# ride_cost: subscription and peak branches

def test_subscription_branches():
    assert ride_cost("standard", 60, False, False) == 40
    assert ride_cost("standard", 60, True, False) == 20


def test_peak_branches():
    assert ride_cost("standard", 30, False, True) == 35
    assert ride_cost("electric", 30, False, True) == 50
    assert ride_cost("cargo", 30, False, True) == 50


def test_long_ride_boundary():
    assert ride_cost("standard", 180, False, False) == 120
    assert ride_cost("standard", 181, False, False) == 240


# dock_status: capacity validation

def test_invalid_capacity():
    with pytest.raises(ValueError):
        dock_status(0, 0)

    with pytest.raises(ValueError):
        dock_status(0, -1)


# dock_status: bike count validation

def test_invalid_bike_counts():
    with pytest.raises(ValueError):
        dock_status(-1, 10)

    with pytest.raises(ValueError):
        dock_status(11, 10)


# dock_status: status branches

def test_all_dock_statuses():
    assert dock_status(0, 10) == "empty"
    assert dock_status(10, 10) == "full"
    assert dock_status(1, 10) == "few bikes"
    assert dock_status(2, 10) == "few bikes"
    assert dock_status(8, 10) == "few slots"
    assert dock_status(9, 10) == "few slots"
    assert dock_status(5, 10) == "available"


# can_unlock: active ride branch

def test_active_ride_branches():
    assert can_unlock(200, True, 25) is False
    assert can_unlock(200, False, 25) is True


# can_unlock: age branches

def test_age_boundaries():
    assert can_unlock(200, False, 15) is False
    assert can_unlock(100, False, 16) is True
    assert can_unlock(100, False, 17) is True
    assert can_unlock(50, False, 18) is True


# can_unlock: balance branches

def test_balance_boundaries():
    assert can_unlock(99, False, 16) is False
    assert can_unlock(100, False, 16) is True
    assert can_unlock(49, False, 18) is False
    assert can_unlock(50, False, 18) is True