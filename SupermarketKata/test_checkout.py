from pytest import fixture, approx
from checkout import Checkout

@fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_can_calculate_current_total(checkout):
    checkout.add_item_price("bananas", 0.20)
    checkout.add_item("bananas")
    subtotal = checkout.subtotal()
    assert subtotal == approx(0.20)