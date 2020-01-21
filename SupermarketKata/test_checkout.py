from pytest import fixture, approx
from checkout import Checkout

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
    checkout.add_discount("banana", 3, 2)
