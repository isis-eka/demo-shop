"""Discount codes: a percentage off the subtotal, with a minimum spend and an expiry date."""
from datetime import date


class DiscountError(Exception):
    pass


CODES = {
    "SAVE10": {"percent": 10, "min_subtotal": 50.00, "expires": date(2099, 12, 31)},
    "SPRING5": {"percent": 5, "min_subtotal": 0.00, "expires": date(2026, 3, 31)},
}


def apply_code(cart, code, today=None):
    """Apply a discount code to the cart and return the new subtotal.

    Raises DiscountError, leaving the cart unchanged, if the code is unknown, expired,
    already used on this cart, or the subtotal is below the code's minimum spend.
    """
    today = today or date.today()
    rule = CODES.get(code)
    if rule is None:
        raise DiscountError(f"unknown code {code}")
    if today > rule["expires"]:
        raise DiscountError(f"code {code} has expired")
    if code in cart.used_codes:
        raise DiscountError(f"code {code} was already used")
    if cart.subtotal() < rule["min_subtotal"]:
        raise DiscountError(f"spend at least ${rule['min_subtotal']:.2f} to use {code}")
    cart.discount = rule["percent"] / 100
    cart.used_codes.add(code)
    return cart.subtotal()
