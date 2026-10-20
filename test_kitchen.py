# Test list:
# [x] 200 g × 3 = 600 g
# [x] Multiplying a quantity does not modify the original
# [x] Two quantities with the same amount are equal (unit coverage follows in A5)
# [ ] 1 oz is not the same as 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz, reduced to grams, using a conversion rate
# [ ] (200 g + 1 oz) × 2
# [ ] Consider hashability if quantities need to be dictionary keys or set members

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)


def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)
    assert flour.times(2) == Quantity(400)
    assert flour == Quantity(200)


def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)
