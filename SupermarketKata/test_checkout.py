from checkout import Checkout

def test_can_add_item_price():
    checkout = Checkout()
    checkout.add_item_price("bananas", "0.20")
