"""
Determines if a shopping list item is eligible for free shipping
"""

def main():
    """Assignment operators"""
    # Set item_name, item_price, quantity, discount_rate, and eligible_items
    item_name = 'banana'
    quantity = 5
    discount_rate = 0.1
    eligible_items = "orange banana carrot"
    item_price = 2  # USD

    """Arithmetic operators"""
    # Calculate subtotal as item_price * quantity
    subtotal = item_price * quantity

    # print item_name, subtotal
    print(f"item_name: {item_name}, subtotal: {subtotal}")

    # Initialize discount to 0
    discount = 0

    """Membership operators"""
    # Check if item_name is in eligible_items string
    # (used to check if an item is eligible for a discount)
    if item_name in eligible_items:
        discount = subtotal * discount_rate

    # print discount
    print(f"discount: {discount}")


    """Comparison operators"""
    # Check if discount is applied (discount > 0)
    was_discount_applied = discount > 0
    print(f"Was the discount applied? {was_discount_applied}.")

    """Logical operators"""
    # Check if free shipping be applied (quantity > 5 AND item_name = 'banana')
    # does_free_shipping_apply = quantity > 5 and item_name == 'banana'
    does_free_shipping_apply = quantity > 5 or item_name == 'banana'
    print(f"Is the item eligible for free shipping? {does_free_shipping_apply}")


if __name__ == '__main__':
    main()