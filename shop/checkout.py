"""Checkout: turns a cart into a receipt, adding Singapore GST."""
from dataclasses import dataclass

GST_RATE = 0.09


class CheckoutError(Exception):
    pass


@dataclass
class Receipt:
    lines: list      # (name, quantity, line total)
    subtotal: float
    gst: float
    total: float

    def text(self):
        rows = [f"{name} x{qty}  ${amount:.2f}" for name, qty, amount in self.lines]
        rows += [f"Subtotal  ${self.subtotal:.2f}", f"GST 9%  ${self.gst:.2f}", f"Total  ${self.total:.2f}"]
        return "\n".join(rows)


def checkout(cart):
    """Return a Receipt for the cart. Raises CheckoutError if the cart is empty."""
    if cart.is_empty():
        raise CheckoutError("cannot check out an empty cart")
    lines = [(item.name, qty, round(item.price * qty, 2)) for item, qty in cart.lines.values()]
    subtotal = cart.subtotal()
    gst = round(subtotal * GST_RATE, 2)
    return Receipt(lines=lines, subtotal=subtotal, gst=gst, total=round(subtotal + gst, 2))
