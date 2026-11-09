from shop.cart import Cart, Item
from shop.checkout import checkout

APPLE = Item("apple", 1.50)
BREAD = Item("bread", 3.20)
JACKET = Item("jacket", 60.00)


def test_receipt_total_includes_gst():
    cart = Cart()
    cart.add_item(JACKET)
    receipt = checkout(cart)
    assert receipt.gst == 5.40
    assert receipt.total == 65.40


def test_receipt_lists_each_item():
    cart = Cart()
    cart.add_item(APPLE, 2)
    cart.add_item(BREAD)
    text = checkout(cart).text()
    assert "apple x2" in text
    assert "bread x1" in text


def test_checkout_empty_cart():
    cart = Cart()
    cart.add_item(APPLE)
    cart.remove_item("apple")
    cart.add_item(BREAD)
    text = checkout(cart).text()
    assert "bread x1" in text
    assert "apple" not in text
