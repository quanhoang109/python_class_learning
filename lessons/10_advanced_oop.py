"""
Lesson 10: Advanced OOP Concepts in Python
==========================================

Advanced object-oriented programming concepts and best practices:
- Composition vs Inheritance
- Mixins
- Descriptors
- Metaclasses (basics)
- SOLID Principles
- Design Patterns Introduction

Key Concepts:
1. Composition over inheritance principle
2. Mixins for code reuse
3. Descriptors for attribute management
4. Metaclasses for class creation
5. SOLID principles for better design
6. Common design patterns

Run this file: python lessons/10_advanced_oop.py
"""

from abc import ABC, abstractmethod
from datetime import datetime


# =============================================================================
# 1. COMPOSITION VS INHERITANCE
# =============================================================================

# BAD APPROACH: Deep inheritance hierarchy
class BadVehicle:
    """Base class."""
    pass

class BadCar(BadVehicle):
    """Car inherits from Vehicle."""
    pass

class BadElectricCar(BadCar):
    """Electric car inherits from Car - getting messy!"""
    pass

class BadSelfDrivingElectricCar(BadElectricCar):
    """Too deep! Hard to maintain and extend."""
    pass


# BETTER APPROACH: Composition
class Engine:
    """Engine component - can be used in any vehicle."""

    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def start(self):
        return f"{self.engine_type} engine starting ({self.horsepower} HP)"

    def stop(self):
        return f"{self.engine_type} engine stopping"


class Battery:
    """Battery component - can be used in electric vehicles."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.charge_level = 100

    def charge(self):
        self.charge_level = 100
        return f"Battery charged to 100% (Capacity: {self.capacity}kWh)"

    def get_range(self):
        return self.capacity * 5  # Simplified: 5 miles per kWh


class AutoPilot:
    """Self-driving component - can be added to any vehicle."""

    def __init__(self, version):
        self.version = version
        self.enabled = False

    def enable(self):
        self.enabled = True
        return f"AutoPilot {self.version} enabled"

    def disable(self):
        self.enabled = False
        return f"AutoPilot {self.version} disabled"


class Vehicle:
    """Vehicle using composition instead of inheritance."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"


class Car(Vehicle):
    """Car composed of engine and optional components."""

    def __init__(self, brand, model, engine):
        super().__init__(brand, model)
        self.engine = engine  # Composition!
        self.autopilot = None  # Optional component

    def start(self):
        return self.engine.start()

    def add_autopilot(self, autopilot):
        """Add autopilot capability through composition."""
        self.autopilot = autopilot


class ElectricCar(Vehicle):
    """Electric car composed of battery and optional components."""

    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery  # Composition!
        self.autopilot = None   # Optional component

    def charge(self):
        return self.battery.charge()

    def get_range(self):
        return self.battery.get_range()

    def add_autopilot(self, autopilot):
        """Add autopilot capability through composition."""
        self.autopilot = autopilot


def demo_composition_vs_inheritance():
    """Demonstrate composition over inheritance."""
    print("\n" + "="*60)
    print("COMPOSITION VS INHERITANCE")
    print("="*60)

    # Create different vehicles with different components
    print("\nRegular car with gas engine:")
    gas_engine = Engine("V8 Gasoline", 450)
    car = Car("Ford", "Mustang", gas_engine)
    print(f"  {car}")
    print(f"  {car.start()}")

    print("\nElectric car with battery:")
    battery = Battery(100)
    tesla = ElectricCar("Tesla", "Model 3", battery)
    print(f"  {tesla}")
    print(f"  {tesla.charge()}")
    print(f"  Range: {tesla.get_range()} miles")

    print("\nAdding autopilot to electric car:")
    autopilot = AutoPilot("v10.2")
    tesla.add_autopilot(autopilot)
    print(f"  {tesla.autopilot.enable()}")

    print("\nBenefits of Composition:")
    print("  - More flexible than inheritance")
    print("  - Components are reusable")
    print("  - Easy to add/remove features")
    print("  - Avoids deep inheritance hierarchies")


# =============================================================================
# 2. MIXINS - Reusable behavior through multiple inheritance
# =============================================================================

class TimestampMixin:
    """Mixin to add timestamp functionality to any class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def touch(self):
        """Update the timestamp."""
        self.updated_at = datetime.now()

    def get_age(self):
        """Get age in seconds."""
        return (datetime.now() - self.created_at).total_seconds()


class SerializableMixin:
    """Mixin to add serialization functionality."""

    def to_dict(self):
        """Convert object to dictionary."""
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith('_')}

    def to_json(self):
        """Convert object to JSON string (simplified)."""
        import json
        data = {}
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                if isinstance(v, datetime):
                    data[k] = v.isoformat()
                else:
                    data[k] = str(v)
        return json.dumps(data, indent=2)


class ValidatableMixin:
    """Mixin to add validation functionality."""

    def is_valid(self):
        """Override this in subclasses."""
        return True

    def validate(self):
        """Validate and raise exception if invalid."""
        if not self.is_valid():
            raise ValueError(f"{self.__class__.__name__} validation failed")


class Article(TimestampMixin, SerializableMixin, ValidatableMixin):
    """Article using multiple mixins."""

    def __init__(self, title, content, author):
        super().__init__()  # Call mixin __init__
        self.title = title
        self.content = content
        self.author = author

    def is_valid(self):
        """Validate article."""
        return (bool(self.title) and
                bool(self.content) and
                bool(self.author) and
                len(self.title) >= 5)

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Product(TimestampMixin, SerializableMixin):
    """Product using timestamp and serialization mixins."""

    def __init__(self, name, price, stock):
        super().__init__()
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        """Update price and timestamp."""
        self.price = new_price
        self.touch()  # From TimestampMixin


def demo_mixins():
    """Demonstrate mixin pattern."""
    print("\n" + "="*60)
    print("MIXINS - Reusable Behavior")
    print("="*60)

    # Article with mixins
    article = Article(
        "Understanding Python Mixins",
        "Mixins are a way to reuse code...",
        "Alice"
    )

    print(f"\nArticle: {article}")
    print(f"  Valid? {article.is_valid()}")
    print(f"  Age: {article.get_age():.2f} seconds")
    print(f"  Dictionary: {article.to_dict()}")

    import time
    time.sleep(0.1)  # Wait a bit
    article.touch()
    print(f"  Age after touch: {article.get_age():.2f} seconds")

    # Product with mixins
    product = Product("Laptop", 999.99, 50)
    print(f"\nProduct: {product.name}")
    print(f"  JSON:\n{product.to_json()}")

    print("\nBenefits of Mixins:")
    print("  - Reuse functionality across unrelated classes")
    print("  - Add features without deep inheritance")
    print("  - Keep concerns separated")
    print("  - Compose behavior from multiple sources")


# =============================================================================
# 3. DESCRIPTORS - Manage attribute access
# =============================================================================

class PositiveNumber:
    """Descriptor that ensures value is positive."""

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        """Called when accessing the attribute."""
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        """Called when setting the attribute."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        instance.__dict__[self.name] = value


class String:
    """Descriptor that validates string length."""

    def __init__(self, name, min_length=0, max_length=100):
        self.name = name
        self.min_length = min_length
        self.max_length = max_length

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, "")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")
        if len(value) < self.min_length:
            raise ValueError(f"{self.name} must be at least {self.min_length} characters")
        if len(value) > self.max_length:
            raise ValueError(f"{self.name} must be at most {self.max_length} characters")
        instance.__dict__[self.name] = value


class BankAccount:
    """Bank account using descriptors for validation."""

    # Descriptors defined at class level
    balance = PositiveNumber("balance")
    account_holder = String("account_holder", min_length=2, max_length=50)

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Uses String descriptor
        self.balance = initial_balance        # Uses PositiveNumber descriptor

    def deposit(self, amount):
        """Deposit money."""
        self.balance += amount  # Descriptor validates!

    def withdraw(self, amount):
        """Withdraw money."""
        self.balance -= amount  # Descriptor validates!

    def __str__(self):
        return f"Account: {self.account_holder}, Balance: ${self.balance:.2f}"


def demo_descriptors():
    """Demonstrate descriptor pattern."""
    print("\n" + "="*60)
    print("DESCRIPTORS - Attribute Management")
    print("="*60)

    account = BankAccount("Alice Johnson", 1000)
    print(f"\n{account}")

    print(f"\nDepositing $500:")
    account.deposit(500)
    print(f"  {account}")

    print(f"\nTrying invalid operations:")

    try:
        print(f"  Setting negative balance:")
        account.balance = -100
    except ValueError as e:
        print(f"    Error: {e}")

    try:
        print(f"  Setting short name:")
        account.account_holder = "A"
    except ValueError as e:
        print(f"    Error: {e}")

    try:
        print(f"  Setting non-string name:")
        account.account_holder = 123
    except TypeError as e:
        print(f"    Error: {e}")

    print("\nBenefits of Descriptors:")
    print("  - Centralized validation logic")
    print("  - Reusable across multiple classes")
    print("  - Clean syntax for users")
    print("  - Powers @property, @classmethod, @staticmethod")


# =============================================================================
# 4. METACLASSES - Classes that create classes (Advanced)
# =============================================================================

class SingletonMeta(type):
    """
    Metaclass that implements Singleton pattern.
    Only one instance of the class can exist.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Called when creating an instance of the class."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """Database connection using Singleton metaclass."""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        print(f"  Creating connection to {connection_string}")

    def query(self, sql):
        return f"Executing: {sql}"


class Logger(metaclass=SingletonMeta):
    """Logger using Singleton pattern."""

    def __init__(self):
        self.logs = []
        print(f"  Creating new logger instance")

    def log(self, message):
        self.logs.append(message)
        print(f"  LOG: {message}")


def demo_metaclasses():
    """Demonstrate metaclasses (basic introduction)."""
    print("\n" + "="*60)
    print("METACLASSES - Classes that Create Classes")
    print("="*60)

    print("\nCreating first database connection:")
    db1 = DatabaseConnection("postgresql://localhost/db1")

    print("\nTrying to create second connection:")
    db2 = DatabaseConnection("postgresql://localhost/db2")

    print(f"\nAre they the same object? {db1 is db2}")
    print(f"  db1: {db1.connection_string}")
    print(f"  db2: {db2.connection_string}")

    print("\nLogger singleton:")
    logger1 = Logger()
    logger1.log("First message")

    logger2 = Logger()
    logger2.log("Second message")

    print(f"\nAre they the same? {logger1 is logger2}")
    print(f"  Logger1 logs: {len(logger1.logs)}")
    print(f"  Logger2 logs: {len(logger2.logs)}")

    print("\nMetaclasses are advanced!")
    print("  - Metaclasses create classes (type is the default metaclass)")
    print("  - Use for: Singletons, validation, registration, etc.")
    print("  - Usually overkill - decorators/functions often better")


# =============================================================================
# 5. SOLID PRINCIPLES
# =============================================================================

# S - SINGLE RESPONSIBILITY PRINCIPLE
# Each class should have only one reason to change

class BadUserManager:
    """BAD: Does too many things!"""

    def create_user(self, name, email):
        pass

    def delete_user(self, user_id):
        pass

    def send_email(self, email, message):  # Not its responsibility!
        pass

    def generate_report(self):  # Not its responsibility!
        pass


# GOOD: Separate responsibilities
class UserRepository:
    """Responsible ONLY for user data management."""

    def __init__(self):
        self.users = {}

    def create(self, user):
        self.users[user.id] = user

    def get(self, user_id):
        return self.users.get(user_id)

    def delete(self, user_id):
        if user_id in self.users:
            del self.users[user_id]


class EmailService:
    """Responsible ONLY for sending emails."""

    def send(self, recipient, message):
        return f"Email sent to {recipient}: {message}"


class ReportGenerator:
    """Responsible ONLY for generating reports."""

    def generate_user_report(self, users):
        return f"Report for {len(users)} users"


# O - OPEN/CLOSED PRINCIPLE
# Open for extension, closed for modification

class Discount(ABC):
    """Abstract discount - can extend with new types."""

    @abstractmethod
    def calculate(self, amount):
        pass


class PercentageDiscount(Discount):
    """Percentage discount - extends Discount."""

    def __init__(self, percent):
        self.percent = percent

    def calculate(self, amount):
        return amount * (self.percent / 100)


class FixedDiscount(Discount):
    """Fixed discount - extends Discount."""

    def __init__(self, amount):
        self.amount = amount

    def calculate(self, amount):
        return min(self.amount, amount)


class SeasonalDiscount(Discount):
    """New discount type - extended without modifying existing code!"""

    def __init__(self, month, percent):
        self.month = month
        self.percent = percent

    def calculate(self, amount):
        if datetime.now().month == self.month:
            return amount * (self.percent / 100)
        return 0


# L - LISKOV SUBSTITUTION PRINCIPLE
# Subclasses should be substitutable for their base classes

class Bird(ABC):
    """Base bird class."""

    @abstractmethod
    def move(self):
        pass


class FlyingBird(Bird):
    """Flying birds can fly."""

    def move(self):
        return "Flying through the air"


class Penguin(Bird):
    """Penguins can't fly - different movement."""

    def move(self):
        return "Swimming in water"  # Still valid movement!


def make_bird_move(bird: Bird):
    """Works with ANY bird - Liskov Substitution."""
    return bird.move()


# I - INTERFACE SEGREGATION PRINCIPLE
# Don't force classes to implement interfaces they don't use

class Printer(ABC):
    """Small, focused interface."""

    @abstractmethod
    def print_document(self, doc):
        pass


class Scanner(ABC):
    """Small, focused interface."""

    @abstractmethod
    def scan_document(self):
        pass


class Fax(ABC):
    """Small, focused interface."""

    @abstractmethod
    def fax_document(self, doc, number):
        pass


class SimplePrinter(Printer):
    """Only implements printing - doesn't need scan/fax."""

    def print_document(self, doc):
        return f"Printing: {doc}"


class AllInOnePrinter(Printer, Scanner, Fax):
    """Implements all interfaces."""

    def print_document(self, doc):
        return f"Printing: {doc}"

    def scan_document(self):
        return "Scanning document"

    def fax_document(self, doc, number):
        return f"Faxing {doc} to {number}"


# D - DEPENDENCY INVERSION PRINCIPLE
# Depend on abstractions, not concretions

class NotificationSender(ABC):
    """Abstract notification sender."""

    @abstractmethod
    def send(self, recipient, message):
        pass


class EmailSender(NotificationSender):
    """Email implementation."""

    def send(self, recipient, message):
        return f"Email to {recipient}: {message}"


class SMSSender(NotificationSender):
    """SMS implementation."""

    def send(self, recipient, message):
        return f"SMS to {recipient}: {message}"


class UserNotifier:
    """Depends on abstraction (NotificationSender), not concrete class."""

    def __init__(self, sender: NotificationSender):
        self.sender = sender  # Can be ANY NotificationSender!

    def notify_user(self, user, message):
        return self.sender.send(user, message)


def demo_solid_principles():
    """Demonstrate SOLID principles."""
    print("\n" + "="*60)
    print("SOLID PRINCIPLES")
    print("="*60)

    print("\nS - Single Responsibility:")
    print("  Each class does ONE thing well")
    repo = UserRepository()
    email = EmailService()
    print(f"  {email.send('user@example.com', 'Welcome!')}")

    print("\nO - Open/Closed:")
    print("  Open for extension, closed for modification")
    amount = 100
    discounts = [
        PercentageDiscount(10),
        FixedDiscount(15),
        SeasonalDiscount(12, 20)  # New type added without changing code!
    ]
    for discount in discounts:
        print(f"  {discount.__class__.__name__}: ${discount.calculate(amount):.2f}")

    print("\nL - Liskov Substitution:")
    print("  Subclasses can replace base class")
    birds = [FlyingBird(), Penguin()]
    for bird in birds:
        print(f"  {bird.__class__.__name__}: {make_bird_move(bird)}")

    print("\nI - Interface Segregation:")
    print("  Small, focused interfaces")
    simple = SimplePrinter()
    all_in_one = AllInOnePrinter()
    print(f"  {simple.print_document('doc.pdf')}")
    print(f"  {all_in_one.scan_document()}")

    print("\nD - Dependency Inversion:")
    print("  Depend on abstractions, not implementations")
    email_notifier = UserNotifier(EmailSender())
    sms_notifier = UserNotifier(SMSSender())
    print(f"  {email_notifier.notify_user('alice@example.com', 'Hello!')}")
    print(f"  {sms_notifier.notify_user('+1-555-0123', 'Hello!')}")


# =============================================================================
# 6. DESIGN PATTERNS INTRODUCTION
# =============================================================================

# STRATEGY PATTERN
class SortStrategy(ABC):
    """Abstract sorting strategy."""

    @abstractmethod
    def sort(self, data):
        pass


class BubbleSort(SortStrategy):
    """Bubble sort strategy."""

    def sort(self, data):
        return f"Bubble sorting {len(data)} items"


class QuickSort(SortStrategy):
    """Quick sort strategy."""

    def sort(self, data):
        return f"Quick sorting {len(data)} items"


class Sorter:
    """Context that uses strategy."""

    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)


# OBSERVER PATTERN
class Observer(ABC):
    """Abstract observer."""

    @abstractmethod
    def update(self, message):
        pass


class EmailObserver(Observer):
    """Email observer."""

    def update(self, message):
        print(f"    Email notification: {message}")


class SMSObserver(Observer):
    """SMS observer."""

    def update(self, message):
        print(f"    SMS notification: {message}")


class Subject:
    """Subject that notifies observers."""

    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# FACTORY PATTERN (already covered in lesson 9, brief example)
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    """Factory for creating animals."""

    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


def demo_design_patterns():
    """Demonstrate common design patterns."""
    print("\n" + "="*60)
    print("DESIGN PATTERNS INTRODUCTION")
    print("="*60)

    print("\nSTRATEGY PATTERN:")
    print("  Define family of algorithms, make them interchangeable")
    data = [5, 2, 8, 1, 9]
    sorter = Sorter(BubbleSort())
    print(f"  {sorter.sort_data(data)}")
    sorter.strategy = QuickSort()  # Change strategy at runtime!
    print(f"  {sorter.sort_data(data)}")

    print("\nOBSERVER PATTERN:")
    print("  One-to-many dependency, notify observers of changes")
    subject = Subject()
    subject.attach(EmailObserver())
    subject.attach(SMSObserver())
    print(f"  Notifying observers:")
    subject.notify("Important update!")

    print("\nFACTORY PATTERN:")
    print("  Create objects without specifying exact class")
    dog = AnimalFactory.create_animal("dog")
    cat = AnimalFactory.create_animal("cat")
    print(f"  Dog says: {dog.speak()}")
    print(f"  Cat says: {cat.speak()}")

    print("\nOther important patterns:")
    print("  - Singleton: One instance only (covered in metaclasses)")
    print("  - Decorator: Add behavior dynamically")
    print("  - Adapter: Make incompatible interfaces work together")
    print("  - Command: Encapsulate requests as objects")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

def print_key_takeaways():
    """Print key learning points."""
    print("\n" + "="*60)
    print("KEY TAKEAWAYS - Advanced OOP")
    print("="*60)

    takeaways = [
        "1. COMPOSITION > INHERITANCE:",
        "   - More flexible and maintainable",
        "   - Favor 'has-a' over 'is-a' relationships",
        "",
        "2. MIXINS:",
        "   - Reuse behavior across unrelated classes",
        "   - Multiple inheritance for functionality",
        "",
        "3. DESCRIPTORS:",
        "   - Manage attribute access at class level",
        "   - Power behind @property, @classmethod, @staticmethod",
        "",
        "4. METACLASSES:",
        "   - Classes that create classes",
        "   - Usually overkill - use sparingly",
        "",
        "5. SOLID PRINCIPLES:",
        "   S - Single Responsibility: One reason to change",
        "   O - Open/Closed: Open for extension, closed for modification",
        "   L - Liskov Substitution: Subclasses are substitutable",
        "   I - Interface Segregation: Small, focused interfaces",
        "   D - Dependency Inversion: Depend on abstractions",
        "",
        "6. DESIGN PATTERNS:",
        "   - Proven solutions to common problems",
        "   - Strategy, Observer, Factory, Singleton, etc.",
        "   - Make code more maintainable and scalable",
        "",
        "7. BEST PRACTICES:",
        "   - Keep classes small and focused",
        "   - Prefer composition over deep inheritance",
        "   - Use abstract classes to define contracts",
        "   - Write code that's easy to test and extend"
    ]

    for takeaway in takeaways:
        print(f"  {takeaway}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*60)
    print("LESSON 10: ADVANCED OOP CONCEPTS")
    print("="*60)

    # Run all demonstrations
    demo_composition_vs_inheritance()
    demo_mixins()
    demo_descriptors()
    demo_metaclasses()
    demo_solid_principles()
    demo_design_patterns()
    print_key_takeaways()

    print("\n" + "="*60)
    print("LESSON COMPLETE!")
    print("="*60)
    print("\nCongratulations! You've completed the Python OOP Tutorial!")
    print("\nNext Steps:")
    print("  1. Review all lessons and run the examples")
    print("  2. Build a project using OOP principles")
    print("  3. Study design patterns in depth")
    print("  4. Practice refactoring procedural code to OOP")
    print("  5. Explore real-world codebases to see OOP in action")
    print("\nHappy coding!")
