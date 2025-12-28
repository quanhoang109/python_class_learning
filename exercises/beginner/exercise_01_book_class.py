"""
Exercise 1: Create a Book Class

Create a `Book` class with the following:
- Attributes: title, author, pages, price, is_available
- Methods:
  - display_info() - print book details
  - apply_discount(percent) - reduce price by percentage
  - borrow() - set is_available to False
  - return_book() - set is_available to True

Test your class with the code at the bottom.

Note: See exercise_01_book_class_pydantic.py for Pydantic version
"""

class Book:
    def __init__(self, title, author, pages, price, is_available=True):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.is_available = is_available

    def display_info(self):
        """Display book information"""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.pages}")
        print(f"Price: ${self.price:.2f}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

    def apply_discount(self, percent):
        """Apply discount with validation (0-100%)"""
        # Validate that percent is a number
        if not isinstance(percent, (int, float)):
            raise ValueError("Discount percent must be a number")
        # Validate that percent is between 0 and 100
        if not 0 <= percent <= 100:
            raise ValueError("Discount percent must be between 0 and 100")

        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount
        print(f"New price after {percent}% discount: ${self.price:.2f}")

    def borrow(self):
        """Borrow the book"""
        if self.is_available:
            self.is_available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        """Return the book"""
        if not self.is_available:
            self.is_available = True
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")


# ============================================================================
# Tests
# ============================================================================

if __name__ == "__main__":
    print("=== Test 1: Normal Usage ===")
    book = Book("Python Basics", "John Smith", 350, 29.99, True)
    book.display_info()
    print()

    print("=== Test 2: Valid Discount (10%) ===")
    book.apply_discount(10)
    print()

    print("=== Test 3: Borrow Book ===")
    book.borrow()
    book.display_info()
    print()

    print("=== Test 4: Return Book ===")
    book.return_book()
    print()

    # Test validation
    print("=== Test 5: Invalid Discount Tests ===")
    try:
        book.apply_discount("invalid")  # Should fail - not a number
    except ValueError as e:
        print(f"✓ Caught error: {e}")

    try:
        book.apply_discount(-10)  # Should fail - negative
    except ValueError as e:
        print(f"✓ Caught error: {e}")

    try:
        book.apply_discount(150)  # Should fail - over 100
    except ValueError as e:
        print(f"✓ Caught error: {e}")

    print("\n✓ All validation tests passed!")
