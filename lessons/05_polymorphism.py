"""
Lesson 5: Polymorphism in Python
==================================

Polymorphism means "many forms" - the ability to use the same interface
for different underlying forms (data types).

In Python, polymorphism allows us to:
1. Use the same method name across different classes
2. Override methods in child classes
3. Use duck typing (if it walks like a duck...)
4. Implement operator overloading

Run this file: python lessons/05_polymorphism.py
"""

from abc import ABC, abstractmethod
import math


# =============================================================================
# 1. METHOD OVERRIDING - Same method name, different implementation
# =============================================================================

class Animal:
    """Base class for animals."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Generic speak method - to be overridden."""
        return f"{self.name} makes a sound"

    def move(self):
        """Generic move method."""
        return f"{self.name} moves"


class Dog(Animal):
    """Dog class - overrides speak method."""

    def speak(self):
        """Dog's version of speak."""
        return f"{self.name} says: Woof! Woof!"

    def move(self):
        return f"{self.name} runs on four legs"


class Cat(Animal):
    """Cat class - overrides speak method."""

    def speak(self):
        """Cat's version of speak."""
        return f"{self.name} says: Meow!"

    def move(self):
        return f"{self.name} walks gracefully"


class Bird(Animal):
    """Bird class - overrides speak method."""

    def speak(self):
        """Bird's version of speak."""
        return f"{self.name} says: Tweet tweet!"

    def move(self):
        return f"{self.name} flies through the air"


def demo_method_overriding():
    """Demonstrate polymorphism through method overriding."""
    print("\n" + "="*60)
    print("POLYMORPHISM - METHOD OVERRIDING")
    print("="*60)

    # Create different animals
    animals = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Bird("Tweety"),
        Animal("Generic")  # Base class
    ]

    # Call the same method on different objects
    # Each object responds differently (polymorphism!)
    for animal in animals:
        print(f"{animal.speak()}")
        print(f"  → {animal.move()}")
        print()


# =============================================================================
# 2. DUCK TYPING - "If it walks like a duck and quacks like a duck..."
# =============================================================================

class Duck:
    """Duck class."""

    def quack(self):
        return "Quack quack!"

    def fly(self):
        return "Duck flies away"


class Person:
    """Person class that can mimic a duck."""

    def quack(self):
        return "I'm quacking like a duck!"

    def fly(self):
        return "I'm flapping my arms"


class Robot:
    """Robot class that can also act like a duck."""

    def quack(self):
        return "QUACK.EXE executed"

    def fly(self):
        return "Activating propellers"


def make_it_quack_and_fly(duck_like_thing):
    """
    This function doesn't care what TYPE the object is,
    it only cares that it HAS the methods quack() and fly()
    This is DUCK TYPING!
    """
    print(f"  {duck_like_thing.quack()}")
    print(f"  {duck_like_thing.fly()}")


def demo_duck_typing():
    """Demonstrate duck typing."""
    print("\n" + "="*60)
    print("DUCK TYPING - Behavior over Type")
    print("="*60)

    # Different types, same interface
    things = [Duck(), Person(), Robot()]

    for thing in things:
        print(f"\n{thing.__class__.__name__}:")
        make_it_quack_and_fly(thing)


# =============================================================================
# 3. POLYMORPHISM WITH ABSTRACT BASE CLASSES
# =============================================================================

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by child classes."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by child classes."""
        pass

    def describe(self):
        """Common method for all shapes."""
        return f"{self.__class__.__name__}: Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    """Triangle shape."""

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


def calculate_total_area(shapes):
    """
    This function works with ANY shape object.
    It doesn't need to know the specific type - just that it has an area() method.
    This is polymorphism!
    """
    total = sum(shape.area() for shape in shapes)
    return total


def demo_abstract_polymorphism():
    """Demonstrate polymorphism with abstract classes."""
    print("\n" + "="*60)
    print("POLYMORPHISM WITH ABSTRACT BASE CLASSES")
    print("="*60)

    # Create different shapes
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        Circle(3)
    ]

    # Polymorphic behavior - same method call, different implementations
    print("\nShape Details:")
    for shape in shapes:
        print(f"  {shape.describe()}")

    # Calculate total area
    total = calculate_total_area(shapes)
    print(f"\nTotal area of all shapes: {total:.2f}")


# =============================================================================
# 4. OPERATOR OVERLOADING - A form of polymorphism
# =============================================================================

class Vector:
    """2D Vector class with operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload + operator."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overload - operator."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Overload * operator for scalar multiplication."""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Overload == operator."""
        return self.x == other.x and self.y == other.y

    def __str__(self):
        """String representation."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Official string representation."""
        return f"Vector({self.x}, {self.y})"


def demo_operator_overloading():
    """Demonstrate operator overloading."""
    print("\n" + "="*60)
    print("OPERATOR OVERLOADING")
    print("="*60)

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"v1 == v2? {v1 == v2}")
    print(f"v1 == Vector(3, 4)? {v1 == Vector(3, 4)}")


# =============================================================================
# 5. REAL-WORLD EXAMPLE: Payment Processing System
# =============================================================================

class PaymentMethod(ABC):
    """Abstract base class for payment methods."""

    @abstractmethod
    def process_payment(self, amount):
        """Process a payment."""
        pass

    @abstractmethod
    def get_transaction_fee(self, amount):
        """Calculate transaction fee."""
        pass


class CreditCard(PaymentMethod):
    """Credit card payment."""

    def __init__(self, card_number, cvv):
        self.card_number = card_number[-4:]  # Store last 4 digits only
        self.cvv = cvv

    def process_payment(self, amount):
        fee = self.get_transaction_fee(amount)
        total = amount + fee
        return f"Credit Card (****{self.card_number}): ${total:.2f} charged (includes ${fee:.2f} fee)"

    def get_transaction_fee(self, amount):
        return amount * 0.029  # 2.9% fee


class DebitCard(PaymentMethod):
    """Debit card payment."""

    def __init__(self, card_number, pin):
        self.card_number = card_number[-4:]
        self.pin = pin

    def process_payment(self, amount):
        fee = self.get_transaction_fee(amount)
        total = amount + fee
        return f"Debit Card (****{self.card_number}): ${total:.2f} charged (includes ${fee:.2f} fee)"

    def get_transaction_fee(self, amount):
        return 0.50  # Flat $0.50 fee


class PayPal(PaymentMethod):
    """PayPal payment."""

    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        fee = self.get_transaction_fee(amount)
        total = amount + fee
        return f"PayPal ({self.email}): ${total:.2f} charged (includes ${fee:.2f} fee)"

    def get_transaction_fee(self, amount):
        return amount * 0.034 + 0.30  # 3.4% + $0.30


class Cryptocurrency(PaymentMethod):
    """Cryptocurrency payment."""

    def __init__(self, wallet_address):
        self.wallet_address = wallet_address[:10] + "..."

    def process_payment(self, amount):
        fee = self.get_transaction_fee(amount)
        total = amount + fee
        return f"Crypto ({self.wallet_address}): ${total:.2f} charged (includes ${fee:.2f} fee)"

    def get_transaction_fee(self, amount):
        return 1.00  # Flat network fee


class PaymentProcessor:
    """Process payments using any payment method (polymorphism!)."""

    def process(self, payment_method, amount):
        """
        This method doesn't care WHAT payment method is used.
        It just calls process_payment() on whatever is passed.
        This is polymorphism in action!
        """
        print(payment_method.process_payment(amount))


def demo_payment_system():
    """Demonstrate polymorphism in payment processing."""
    print("\n" + "="*60)
    print("REAL-WORLD EXAMPLE: Payment Processing")
    print("="*60)

    # Create payment processor
    processor = PaymentProcessor()

    # Create different payment methods
    payment_methods = [
        CreditCard("1234567890123456", "123"),
        DebitCard("9876543210987654", "4321"),
        PayPal("user@example.com"),
        Cryptocurrency("1A2B3C4D5E6F7G8H9I0J")
    ]

    # Process same amount with different methods
    amount = 100.00
    print(f"\nProcessing ${amount:.2f} payment with different methods:\n")

    for method in payment_methods:
        processor.process(method, amount)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

def print_key_takeaways():
    """Print key learning points."""
    print("\n" + "="*60)
    print("KEY TAKEAWAYS - Polymorphism")
    print("="*60)

    takeaways = [
        "1. Polymorphism = Same interface, different implementations",
        "2. Method Overriding: Child classes customize inherited methods",
        "3. Duck Typing: 'If it looks like a duck...' - behavior over type",
        "4. Abstract Classes: Define contracts that subclasses must follow",
        "5. Operator Overloading: Make objects work with built-in operators",
        "6. Benefits: Flexible code, easy to extend, cleaner design"
    ]

    for takeaway in takeaways:
        print(f"  ✓ {takeaway}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*60)
    print("LESSON 5: POLYMORPHISM IN PYTHON")
    print("="*60)

    # Run all demonstrations
    demo_method_overriding()
    demo_duck_typing()
    demo_abstract_polymorphism()
    demo_operator_overloading()
    demo_payment_system()
    print_key_takeaways()

    print("\n" + "="*60)
    print("LESSON COMPLETE!")
    print("="*60)
    print("\nNext: Lesson 6 - Abstraction")
    print("Run: python lessons/06_abstraction.py")
