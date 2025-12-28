"""
Lesson 8: Properties in Python
===============================

Properties provide a way to customize access to instance attributes.
They allow you to use simple attribute access syntax while running code
behind the scenes (validation, computation, etc.).

Key Concepts:
1. @property decorator for getters
2. @property.setter for setters
3. @property.deleter for deleters
4. Read-only properties
5. Computed properties
6. Lazy properties
7. Property validation

Run this file: python lessons/08_properties.py
"""


# =============================================================================
# 1. BASIC PROPERTIES - @property decorator
# =============================================================================

class Temperature:
    """Temperature class with property for Celsius/Fahrenheit conversion."""

    def __init__(self, celsius):
        self._celsius = celsius  # Private attribute (by convention)

    @property
    def celsius(self):
        """
        Getter method using @property decorator.
        Now we can use: temp.celsius instead of temp.celsius()
        """
        print("    (Getting celsius value)")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """
        Setter method using @property.setter decorator.
        Now we can use: temp.celsius = 25 instead of temp.set_celsius(25)
        """
        print(f"    (Setting celsius to {value})")
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property - calculated on the fly."""
        print("    (Computing fahrenheit from celsius)")
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit."""
        print(f"    (Converting {value}°F to celsius)")
        if value < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
        self._celsius = (value - 32) * 5/9


def demo_basic_properties():
    """Demonstrate basic property usage."""
    print("\n" + "="*60)
    print("BASIC PROPERTIES")
    print("="*60)

    temp = Temperature(25)

    # Using properties like attributes (not methods!)
    print(f"\nGetting temperature:")
    print(f"  Celsius: {temp.celsius}°C")
    print(f"  Fahrenheit: {temp.fahrenheit}°F")

    print(f"\nSetting temperature to 30°C:")
    temp.celsius = 30
    print(f"  Celsius: {temp.celsius}°C")
    print(f"  Fahrenheit: {temp.fahrenheit}°F")

    print(f"\nSetting temperature to 68°F:")
    temp.fahrenheit = 68
    print(f"  Celsius: {temp.celsius}°C")
    print(f"  Fahrenheit: {temp.fahrenheit}°F")

    # Validation in action
    print(f"\nTrying to set invalid temperature:")
    try:
        temp.celsius = -300  # Below absolute zero!
    except ValueError as e:
        print(f"  Error: {e}")


# =============================================================================
# 2. READ-ONLY PROPERTIES
# =============================================================================

class Circle:
    """Circle with read-only computed properties."""

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Radius can be read and modified."""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def diameter(self):
        """Read-only property - no setter defined."""
        return self._radius * 2

    @property
    def area(self):
        """Read-only computed property."""
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        """Read-only computed property."""
        import math
        return 2 * math.pi * self._radius


def demo_readonly_properties():
    """Demonstrate read-only properties."""
    print("\n" + "="*60)
    print("READ-ONLY PROPERTIES")
    print("="*60)

    circle = Circle(5)

    print(f"\nCircle with radius {circle.radius}:")
    print(f"  Diameter: {circle.diameter:.2f}")
    print(f"  Area: {circle.area:.2f}")
    print(f"  Circumference: {circle.circumference:.2f}")

    # Can modify radius
    print(f"\nChanging radius to 10:")
    circle.radius = 10
    print(f"  New diameter: {circle.diameter:.2f}")
    print(f"  New area: {circle.area:.2f}")

    # Cannot modify computed properties
    print(f"\nTrying to set diameter directly:")
    try:
        circle.diameter = 30  # This will fail!
    except AttributeError as e:
        print(f"  Error: can't set attribute (no setter defined)")


# =============================================================================
# 3. PROPERTY WITH VALIDATION
# =============================================================================

class Person:
    """Person class with validated properties."""

    def __init__(self, name, age, email):
        # Using setters for validation even in __init__
        self.name = name    # Calls name.setter
        self.age = age      # Calls age.setter
        self.email = email  # Calls email.setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        """Validate name is not empty."""
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        """Validate age is reasonable."""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        """Validate email format."""
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        self._email = value.lower()

    @property
    def is_adult(self):
        """Read-only computed property."""
        return self._age >= 18


def demo_validation_properties():
    """Demonstrate property validation."""
    print("\n" + "="*60)
    print("PROPERTIES WITH VALIDATION")
    print("="*60)

    # Create valid person
    person = Person("Alice Smith", 30, "Alice@Example.com")
    print(f"\nCreated person:")
    print(f"  Name: {person.name}")
    print(f"  Age: {person.age}")
    print(f"  Email: {person.email}")  # Automatically lowercased
    print(f"  Is adult: {person.is_adult}")

    # Test various validations
    print(f"\nTesting validations:")

    print(f"  Trying empty name:")
    try:
        person.name = "  "
    except ValueError as e:
        print(f"    Error: {e}")

    print(f"  Trying invalid age:")
    try:
        person.age = 200
    except ValueError as e:
        print(f"    Error: {e}")

    print(f"  Trying invalid email:")
    try:
        person.email = "invalid-email"
    except ValueError as e:
        print(f"    Error: {e}")

    # Valid updates work fine
    print(f"\nValid update:")
    person.age = 25
    print(f"  Age updated to: {person.age}")
    print(f"  Is adult: {person.is_adult}")


# =============================================================================
# 4. PROPERTY DELETER
# =============================================================================

class CachedWebPage:
    """Web page with cached content."""

    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        """Get content, fetch if not cached."""
        if self._content is None:
            print(f"    Fetching content from {self.url}...")
            # Simulate fetching from web
            self._content = f"Content from {self.url}"
        else:
            print(f"    Returning cached content")
        return self._content

    @content.setter
    def content(self, value):
        """Manually set content."""
        print(f"    Manually setting content")
        self._content = value

    @content.deleter
    def content(self):
        """
        Delete cached content using @property.deleter.
        Can now use: del obj.content
        """
        print(f"    Clearing cached content")
        self._content = None


def demo_property_deleter():
    """Demonstrate property deleter."""
    print("\n" + "="*60)
    print("PROPERTY DELETER")
    print("="*60)

    page = CachedWebPage("https://example.com")

    print(f"\nFirst access (will fetch):")
    print(f"  {page.content}")

    print(f"\nSecond access (cached):")
    print(f"  {page.content}")

    print(f"\nDeleting cache:")
    del page.content  # Calls deleter

    print(f"\nThird access (will fetch again):")
    print(f"  {page.content}")


# =============================================================================
# 5. LAZY PROPERTIES (Computed Once)
# =============================================================================

class DataAnalyzer:
    """Analyzer with expensive computed properties."""

    def __init__(self, data):
        self.data = data
        self._mean = None
        self._median = None

    @property
    def mean(self):
        """
        Lazy property - computed only once when first accessed.
        Cached for subsequent accesses.
        """
        if self._mean is None:
            print("    Computing mean (expensive operation)...")
            self._mean = sum(self.data) / len(self.data)
        else:
            print("    Returning cached mean")
        return self._mean

    @property
    def median(self):
        """Lazy property for median."""
        if self._median is None:
            print("    Computing median (expensive operation)...")
            sorted_data = sorted(self.data)
            n = len(sorted_data)
            if n % 2 == 0:
                self._median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
            else:
                self._median = sorted_data[n//2]
        else:
            print("    Returning cached median")
        return self._median

    def add_value(self, value):
        """Add value and invalidate cache."""
        self.data.append(value)
        # Invalidate cache when data changes
        self._mean = None
        self._median = None


def demo_lazy_properties():
    """Demonstrate lazy properties."""
    print("\n" + "="*60)
    print("LAZY PROPERTIES (Computed Once)")
    print("="*60)

    analyzer = DataAnalyzer([10, 20, 30, 40, 50])

    print(f"\nFirst access to mean:")
    print(f"  Mean: {analyzer.mean}")

    print(f"\nSecond access to mean (cached):")
    print(f"  Mean: {analyzer.mean}")

    print(f"\nFirst access to median:")
    print(f"  Median: {analyzer.median}")

    print(f"\nSecond access to median (cached):")
    print(f"  Median: {analyzer.median}")

    print(f"\nAdding new value (invalidates cache):")
    analyzer.add_value(60)

    print(f"\nAccessing mean again (recomputes):")
    print(f"  Mean: {analyzer.mean}")


# =============================================================================
# 6. REAL-WORLD EXAMPLE: Bank Account with Properties
# =============================================================================

class BankAccount:
    """Bank account with comprehensive property usage."""

    # Class variable for interest rate
    _interest_rate = 0.02  # 2%

    def __init__(self, account_number, owner, initial_balance=0):
        self._account_number = account_number
        self._owner = owner
        self._balance = initial_balance
        self._transactions = []

    @property
    def account_number(self):
        """Read-only account number."""
        return self._account_number

    @property
    def owner(self):
        """Read-only owner name."""
        return self._owner

    @property
    def balance(self):
        """
        Read-only balance (can't be set directly).
        Must use deposit() or withdraw() methods.
        """
        return self._balance

    @property
    def formatted_balance(self):
        """Computed property for formatted balance."""
        return f"${self._balance:,.2f}"

    @property
    def interest_earned(self):
        """Computed property for interest earned."""
        return self._balance * self._interest_rate

    @property
    def balance_with_interest(self):
        """Computed property for balance with interest."""
        return self._balance + self.interest_earned

    @property
    def transaction_count(self):
        """Number of transactions."""
        return len(self._transactions)

    @property
    def average_transaction(self):
        """Average transaction amount."""
        if not self._transactions:
            return 0
        return sum(self._transactions) / len(self._transactions)

    @classmethod
    @property
    def interest_rate(cls):
        """Class property for interest rate."""
        return cls._interest_rate

    def deposit(self, amount):
        """Deposit money."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(amount)

    def withdraw(self, amount):
        """Withdraw money."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transactions.append(-amount)

    def __str__(self):
        return f"Account {self.account_number}: {self.owner} - {self.formatted_balance}"


def demo_bank_account():
    """Demonstrate comprehensive property usage."""
    print("\n" + "="*60)
    print("REAL-WORLD EXAMPLE: Bank Account")
    print("="*60)

    account = BankAccount("12345", "Alice Johnson", 1000)

    print(f"\n{account}")
    print(f"  Balance: {account.formatted_balance}")
    print(f"  Interest earned: ${account.interest_earned:.2f}")
    print(f"  Balance with interest: ${account.balance_with_interest:.2f}")

    # Make some transactions
    print(f"\nMaking transactions:")
    account.deposit(500)
    print(f"  Deposited $500")
    account.deposit(250)
    print(f"  Deposited $250")
    account.withdraw(300)
    print(f"  Withdrew $300")

    print(f"\nAccount status:")
    print(f"  {account}")
    print(f"  Transaction count: {account.transaction_count}")
    print(f"  Average transaction: ${account.average_transaction:.2f}")

    # Try to modify read-only properties
    print(f"\nTrying to modify read-only properties:")
    try:
        account.balance = 5000  # Can't set directly!
    except AttributeError:
        print(f"  Error: can't set balance directly (must use deposit/withdraw)")

    try:
        account.owner = "Bob"  # Can't change owner!
    except AttributeError:
        print(f"  Error: can't change owner (read-only)")


# =============================================================================
# 7. PROPERTIES VS METHODS - When to Use What
# =============================================================================

class Rectangle:
    """Demonstrating when to use properties vs methods."""

    def __init__(self, width, height):
        self._width = width
        self._height = height

    # USE PROPERTY: Simple attribute access, no parameters needed
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    # USE PROPERTY: Computed values without parameters
    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    # USE METHOD: Requires parameters or performs action
    def scale(self, factor):
        """Scale rectangle by a factor - needs parameter, use method."""
        self._width *= factor
        self._height *= factor

    def fits_inside(self, other):
        """Check if fits inside another rectangle - needs parameter, use method."""
        return self._width <= other.width and self._height <= other.height

    def __str__(self):
        return f"Rectangle({self._width}x{self._height})"


def demo_properties_vs_methods():
    """Demonstrate when to use properties vs methods."""
    print("\n" + "="*60)
    print("PROPERTIES VS METHODS - When to Use What")
    print("="*60)

    rect1 = Rectangle(10, 5)
    rect2 = Rectangle(15, 8)

    print(f"\nRectangle 1: {rect1}")
    print(f"  Width: {rect1.width}")          # Property (no parentheses)
    print(f"  Height: {rect1.height}")        # Property
    print(f"  Area: {rect1.area}")            # Property (computed)
    print(f"  Perimeter: {rect1.perimeter}")  # Property (computed)

    print(f"\nRectangle 2: {rect2}")

    print(f"\nUsing methods (require parameters or perform actions):")
    rect1.scale(2)                            # Method (has parameter)
    print(f"  After scaling by 2: {rect1}")
    print(f"  Fits inside rect2? {rect1.fits_inside(rect2)}")  # Method (has parameter)

    print(f"\nGuidelines:")
    print(f"  - Use PROPERTY: Simple attribute access, no parameters")
    print(f"  - Use PROPERTY: Computed values (area, total, etc.)")
    print(f"  - Use METHOD: Requires parameters")
    print(f"  - Use METHOD: Performs significant action or mutation")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

def print_key_takeaways():
    """Print key learning points."""
    print("\n" + "="*60)
    print("KEY TAKEAWAYS - Properties")
    print("="*60)

    takeaways = [
        "1. Properties provide attribute-like access with method functionality",
        "2. @property decorator creates getter method",
        "3. @property.setter creates setter method with validation",
        "4. @property.deleter creates deleter method",
        "5. Read-only properties: define getter but no setter",
        "6. Computed properties: calculate values on-the-fly",
        "7. Lazy properties: compute once, cache the result",
        "8. Use properties for: simple access, validation, computed values",
        "9. Use methods for: operations with parameters, significant actions",
        "10. Properties make code cleaner and more Pythonic"
    ]

    for takeaway in takeaways:
        print(f"  {takeaway}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*60)
    print("LESSON 8: PROPERTIES IN PYTHON")
    print("="*60)

    # Run all demonstrations
    demo_basic_properties()
    demo_readonly_properties()
    demo_validation_properties()
    demo_property_deleter()
    demo_lazy_properties()
    demo_bank_account()
    demo_properties_vs_methods()
    print_key_takeaways()

    print("\n" + "="*60)
    print("LESSON COMPLETE!")
    print("="*60)
    print("\nNext: Lesson 9 - Class Methods and Static Methods")
    print("Run: python lessons/09_class_methods.py")
