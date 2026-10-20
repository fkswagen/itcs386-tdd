import pytest
from shipping import shipping_fee


# Rule 1: zero and negative weights must raise ValueError.
@pytest.mark.parametrize("weight", [-1, 0])
def test_non_positive_weight_is_rejected(weight):
    with pytest.raises(ValueError, match="more than 0"):
        shipping_fee(weight)


# Rule 2: exactly 1 kg must still cost 40 baht.
@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),
    (1, 40),
])
def test_weight_up_to_one_kg(weight, expected):
    assert shipping_fee(weight) == expected


@pytest.mark.parametrize("weight, expected", [
    (1.1, 60),
    (3, 60),
    (5, 60),
])
def test_weight_over_one_up_to_five_kg(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 4: every started kilogram above 5 kg must be charged.
@pytest.mark.parametrize("weight, expected", [
    (5.2, 70),
    (6, 70),
    (6.2, 80),
])
def test_weight_over_five_kg(weight, expected):
    assert shipping_fee(weight) == expected