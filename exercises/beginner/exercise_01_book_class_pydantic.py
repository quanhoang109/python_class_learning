"""
Exercise 1: Create a Book Class (Pydantic Version)

This version uses Pydantic for automatic validation.
To use this, first install pydantic: pip install pydantic

Benefits of Pydantic:
- Automatic type validation
- Field constraints (gt, lt, ge, le)
- Data serialization/deserialization
- Better error messages
"""
from pydantic import BaseModel, Field, field_validator, ValidationError

class Book(BaseModel):
    """Book class with Pydantic validation"""
    title: str
    author: str
    pages: int = Field(gt=0, description="Number of pages must be positive")
    price: float = Field(gt=0, description="Price must be positive")
    is_available: bool = True

    # Allow mutation for methods like apply_discount
    class Config:
        validate_assignment = True

    @field_validator('price')
    @classmethod
    def price_must_be_positive(cls, v):
        """Additional custom validation for price"""
        if v <= 0:
            raise ValueError('Price must be positive')
        return v

    def display_info(self):
        """Display book information"""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.pages}")
        print(f"Price: ${self.price:.2f}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")

    def apply_discount(self, percent: float):
        """Apply discount with validation (0-100%)"""
        if not isinstance(percent, (int, float)):
            raise ValueError("Discount percent must be a number")
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
    book = Book(title="Python Basics", author="John Smith", pages=350, price=29.99)
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

    print("\n=== Test 6: Pydantic Validation Tests ===")
    try:
        invalid_book = Book(title="Test", author="Test", pages=-5, price=10.0)
    except ValidationError as e:
        print(f"✓ Caught Pydantic error for negative pages")

    try:
        invalid_book = Book(title="Test", author="Test", pages=100, price=-10.0)
    except ValidationError as e:
        print(f"✓ Caught Pydantic error for negative price")

    try:
        invalid_book = Book(title="Test", author="Test", pages="not a number", price=10.0)
    except ValidationError as e:
        print(f"✓ Caught Pydantic error for invalid pages type")

    print("\n=== Test 7: Pydantic JSON Serialization ===")
    # Extra Pydantic feature: JSON serialization
    book_dict = book.model_dump()
    print(f"Book as dict: {book_dict}")

    book_json = book.model_dump_json()
    print(f"Book as JSON: {book_json}")

    print("\n✓ All validation tests passed!")
    print("\n💡 Pydantic provides:")
    print("  - Automatic type checking")
    print("  - Field constraints (gt, lt, ge, le)")
    print("  - Custom validators with @field_validator")
    print("  - JSON serialization/deserialization")
    print("  - Better error messages")
