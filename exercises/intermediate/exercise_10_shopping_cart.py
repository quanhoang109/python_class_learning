"""
Exercise 10: Shopping Cart

Create an e-commerce shopping cart:

Class `Product`:
- Attributes: name, price, quantity_available
- Methods: reduce_stock(amount), display()

Class `CartItem`:
- Attributes: product, quantity
- Methods: get_subtotal()

Class `ShoppingCart`:
- Attributes: items (list of CartItems)
- Methods:
  - add_item(product, quantity) - check stock availability
  - remove_item(product_name)
  - get_total() - sum of all subtotals
  - checkout() - display items and total
"""

# TODO: Write your Product, CartItem, and ShoppingCart classes here


# Test code (uncomment when ready)
# laptop = Product("Laptop", 999.99, 5)
# mouse = Product("Mouse", 29.99, 10)
#
# cart = ShoppingCart()
# cart.add_item(laptop, 1)
# cart.add_item(mouse, 2)
# cart.checkout()
