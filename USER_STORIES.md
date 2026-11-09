# User stories

## US1: Add items to the cart
*As a shopper, I can add items to my cart, so that I can buy more than one thing at once.*

- **AC1.1** Given an empty cart, when the shopper adds 2 of an item, then the cart holds 2 of that item.
- **AC1.2** Given a cart, when the shopper adds an item with a quantity of 0 or less, then a ValueError is raised and the cart is unchanged.

## US2: Use a discount code
*As a shopper, I can apply a discount code, so that I pay less.*

- **AC2.1** Given a cart with a subtotal of $50 or more, when the shopper applies the code SAVE10, then the subtotal drops by 10%.
- **AC2.2** Given an expired discount code, when the shopper applies it, then an "expired" error is raised and the subtotal is unchanged.
- **AC2.3** Given a discount code that was already used on the cart, when the shopper applies it again, then it is rejected with an error.

## US3: Check out
*As a shopper, I can check out, so that I get a receipt with the amount to pay.*

- **AC3.1** Given a cart with items, when the shopper checks out, then the receipt total is the subtotal plus 9% GST.
- **AC3.2** Given an empty cart, when the shopper checks out, then an error is raised and no receipt is created.
