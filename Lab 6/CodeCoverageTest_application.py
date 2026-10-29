import pytest
from pizza_order import pizza_price, order_discount, delivery_status


def test_small_plain_pizza():
    assert pizza_price("small", 0, False) == 200


def test_medium_pizza_with_toppings():
    assert pizza_price("medium", 2, False) == 430


def test_large_pizza_more_than_three_toppings():
    assert pizza_price("large", 5, False) == 680


def test_cheese_burst_medium():
    assert pizza_price("medium", 1, True) == 490


def test_invalid_size():
    with pytest.raises(ValueError):
        pizza_price("extra-large", 1, False)


def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("medium", -1, False)


def test_cheese_burst_small_rejected():
    with pytest.raises(ValueError):
        pizza_price("small", 0, True)


def test_order_below_300():
    assert order_discount(250, "monday", False) == 0


def test_tuesday_discount():
    assert order_discount(400, "tuesday", False) == 200


def test_saturday_discount():
    assert order_discount(400, "saturday", False) == 0


def test_sunday_discount():
    assert order_discount(400, "sunday", False) == 0


def test_regular_weekday_discount():
    assert order_discount(400, "monday", False) == 40


def test_student_discount():
    assert order_discount(400, "monday", True) == 90


def test_not_deliverable():
    assert delivery_status(20, 11) == "not deliverable"


def test_on_time_delivery():
    assert delivery_status(30, 5) == "on time"


def test_late_delivery():
    assert delivery_status(40, 5) == "late"


def test_free_pizza():
    assert delivery_status(50, 5) == "free pizza"