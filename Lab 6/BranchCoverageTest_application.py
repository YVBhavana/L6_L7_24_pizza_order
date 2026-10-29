
import pytest
from pizza_order import pizza_price, order_discount, delivery_status


@pytest.mark.parametrize("size, expected", [
    ("small", 200),
    ("medium", 350),
    ("large", 500),
])
def test_valid_pizza_sizes(size, expected):
    assert pizza_price(size, 0, False) == expected


def test_invalid_size():
    with pytest.raises(ValueError):
        pizza_price("extra-large", 0, False)


@pytest.mark.parametrize("toppings, expected", [
    (0, 350),
    (3, 470),
    (4, 500),
    (5, 530),
])
def test_topping_pricing(toppings, expected):
    assert pizza_price("medium", toppings, False) == expected


def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("medium", -1, False)


def test_cheese_burst_medium():
    assert pizza_price("medium", 0, True) == 450


def test_cheese_burst_large():
    assert pizza_price("large", 0, True) == 600


def test_cheese_burst_small_rejected():
    with pytest.raises(ValueError):
        pizza_price("small", 0, True)


def test_order_below_300():
    assert order_discount(299, "monday", False) == 0


def test_order_exactly_300():
    assert order_discount(300, "monday", False) == 30


def test_tuesday_discount():
    assert order_discount(400, "tuesday", False) == 200


@pytest.mark.parametrize("day", ["saturday", "sunday"])
def test_weekend_discount(day):
    assert order_discount(400, day, False) == 0


def test_regular_weekday_discount():
    assert order_discount(400, "monday", False) == 40


def test_student_discount():
    assert order_discount(400, "monday", True) == 90


def test_non_student_discount():
    assert order_discount(400, "monday", False) == 40


def test_distance_above_10_km():
    assert delivery_status(20, 10.1) == "not deliverable"


def test_distance_exactly_10_km():
    assert delivery_status(30, 10) == "on time"


def test_delivery_at_30_minutes():
    assert delivery_status(30, 5) == "on time"


def test_delivery_at_31_minutes():
    assert delivery_status(31, 5) == "late"


def test_delivery_at_45_minutes():
    assert delivery_status(45, 5) == "late"


def test_delivery_above_45_minutes():
    assert delivery_status(46, 5) == "free pizza"
