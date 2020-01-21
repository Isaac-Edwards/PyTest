import pytest
from checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_can_add_item_price(checkout):
    checkout.add_item_price("bananas", "0.20")

def test_can_add_item(checkout):
    checkout.add_item("bananas")
