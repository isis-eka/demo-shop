"""A shopping cart: items, quantities and the subtotal."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    price: float  # unit price in dollars


class Cart:
    def __init__(self):
        self.lines = {}          # item name -> [Item, quantity]
        self.used_codes = set()  # discount codes already applied to this cart
        self.discount = 0.0      # fraction taken off the subtotal, e.g. 0.10

    def add_item(self, item, quantity=1):
        if quantity <= 0:
            raise ValueError("quantity must be at least 1")
        if item.name in self.lines:
            self.lines[item.name][1] += quantity
        else:
            self.lines[item.name] = [item, quantity]

    def remove_item(self, name):
        if name not in self.lines:
            raise KeyError(f"{name} is not in the cart")
        del self.lines[name]

    def quantity(self, name):
        return self.lines[name][1] if name in self.lines else 0

    def is_empty(self):
        return not self.lines

    def subtotal(self):
        gross = sum(item.price * qty for item, qty in self.lines.values())
        return round(gross * (1 - self.discount), 2)
