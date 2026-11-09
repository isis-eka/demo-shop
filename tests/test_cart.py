import pytest

from shop.cart import Cart, Item

APPLE = Item("apple", 1.50)
BREAD = Item("bread", 3.20)


def test_add_item():
    cart = Cart()
    cart.add_item(APPLE, 2)
    assert cart.quantity("apple") == 2


def test_add_same_item_twice_adds_up():
    cart = Cart()
    cart.add_item(APPLE, 1)
    cart.add_item(APPLE, 2)
    assert cart.quantity("apple") == 3


def test_subtotal():
    cart = Cart()
    cart.add_item(APPLE, 2)
    cart.add_item(BREAD)
    assert cart.subtotal() == 6.20


def test_remove_item():
    cart = Cart()
    cart.add_item(APPLE)
    cart.remove_item("apple")
    assert cart.is_empty()


def test_remove_missing_item():
    cart = Cart()
    with pytest.raises(KeyError):
        cart.remove_item("apple")
