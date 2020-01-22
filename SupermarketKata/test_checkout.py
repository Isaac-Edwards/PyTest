from pytest import fixture, approx, raises
from checkout import Checkout, PriceException

@fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("banana", 0.20)
    checkout.add_item_price("milk", 1)
    checkout.add_item_price("TV", 999)
    return checkout

def test_can_calculate_current_total(checkout):
    checkout.add_item("banana")
    subtotal = checkout.subtotal()
    assert subtotal == approx(0.20)

def test_can_calculate_total_for_multiple_items(checkout):
    checkout.add_item("banana")
    checkout.add_item("milk")
    checkout.add_item("TV")

    subtotal = checkout.subtotal()
    assert subtotal == approx(1000.20)

def test_can_add_price_but_not_item_and_total_stays_zero(checkout):
    checkout.add_item_price("banana", 0.20)
    subtotal = checkout.subtotal()
    assert subtotal == 0

def test_when_same_item_added_multiple_times_subtotal_is_correct(checkout):
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    subtotal = checkout.subtotal()
    assert subtotal == approx(0.80)

def test_can_add_discount_rules(checkout):
    checkout.add_discount("banana", 3, 0.40)

def test_can_apply_discount_rules_and_get_correct_subtotal(checkout):
    checkout.add_discount("banana", 3, 0.40)
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    assert checkout.subtotal() == approx(0.40)

def test_can_exceed_discount_quantities_and_get_correct_subtotal(checkout):
    checkout.add_discount("banana", 3, 0.40)
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    assert checkout.subtotal() == approx(0.60)

def test_if_discount_quantities_not_achieved_still_get_correct_subtotal(checkout):
    checkout.add_discount("banana", 3, 0.40)
    checkout.add_item("banana")
    assert checkout.subtotal() == approx(0.20)

def test_can_double_discount_quantities_and_get_discount_twice(checkout):
    checkout.add_discount("banana", 3, 0.40)
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    checkout.add_item("banana")
    assert checkout.subtotal() == approx(0.80)

def test_exception_thrown_when_item_added_with_no_price(checkout):
    with raises(PriceException):
        checkout.add_item("Isaac Edwards")