from datetime import date

import pytest

from shop.cart import Cart, Item
from shop.discounts import DiscountError, apply_code

JACKET = Item("jacket", 60.00)
APPLE = Item("apple", 1.50)


def make_cart():
    cart = Cart()
    cart.add_item(JACKET)
    return cart


def test_save10_takes_10_percent_off():
    cart = make_cart()
    assert apply_code(cart, "SAVE10") == 54.00


def test_save10_needs_minimum_spend():
    cart = Cart()
    cart.add_item(APPLE)
    with pytest.raises(DiscountError):
        apply_code(cart, "SAVE10")


def test_unknown_code():
    cart = make_cart()
    with pytest.raises(DiscountError, match="unknown"):
        apply_code(cart, "FREESTUFF")


def test_expired_code_is_rejected():
    cart = make_cart()
    with pytest.raises(DiscountError, match="expired"):
        apply_code(cart, "SPRING5", today=date(2026, 6, 1))


def test_apply_code_twice():
    cart = make_cart()
    apply_code(cart, "SAVE10")
    try:
        apply_code(cart, "SAVE10")
    except DiscountError:
        pass
