"""
Python OOP Exercise Solutions
Complete solutions for all exercises in EXERCISES.md
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import math

# ==============================================================================
# BEGINNER EXERCISES
# ==============================================================================

# Exercise 1: Book Class
class Book:
    """Represents a book with title, author, pages, price, and availability."""

    def __init__(self, title, author, pages, price, is_available=True):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.is_available = is_available

    def display_info(self):
        """Display book information."""
        status = "Available" if self.is_available else "Borrowed"
        print(f"\n--- Book Info ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: ${self.price:.2f}")
        print(f"Status: {status}")

    def apply_discount(self, percent):
        """Apply a discount to the book price."""
        if 0 <= percent <= 100:
            discount = self.price * (percent / 100)
            self.price -= discount
            print(f"Applied {percent}% discount. New price: ${self.price:.2f}")
        else:
            print("Invalid discount percentage")

    def borrow(self):
        """Borrow the book."""
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        """Return the book."""
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed.")


# Exercise 2: Rectangle Class
class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter."""
        return 2 * (self.width + self.height)

    def is_square(self):
        """Check if the rectangle is a square."""
        return self.width == self.height

    def scale(self, factor):
        """Scale both dimensions by a factor."""
        self.width *= factor
        self.height *= factor

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# Exercise 3: Student Class
class Student:
    """Represents a student with name, ID, and grades."""

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        """Add a grade with validation (0-100)."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade {grade} for {self.name}")
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def get_average(self):
        """Calculate and return the average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Convert average to letter grade."""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def display_report_card(self):
        """Display student's complete report card."""
        print(f"\n--- Report Card ---")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")


# Exercise 4: Counter Class
class Counter:
    """A counter with class-level tracking of total instances."""

    total_counters = 0  # Class attribute

    def __init__(self):
        self.count = 0
        Counter.total_counters += 1

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def decrement(self):
        """Decrement the counter by 1."""
        self.count -= 1

    def reset(self):
        """Reset the counter to 0."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count

    @classmethod
    def get_total_counters(cls):
        """Return the total number of Counter instances created."""
        return cls.total_counters


# Exercise 5: Temperature Class
class Temperature:
    """Temperature converter with multiple unit support."""

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        """Convert to Fahrenheit."""
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        """Convert to Kelvin."""
        return self.celsius + 273.15

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Create Temperature instance from Fahrenheit."""
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)

    @classmethod
    def from_kelvin(cls, kelvin):
        """Create Temperature instance from Kelvin."""
        celsius = kelvin - 273.15
        return cls(celsius)

    @staticmethod
    def is_freezing(celsius):
        """Check if temperature is at or below freezing."""
        return celsius <= 0

    def __str__(self):
        return f"{self.celsius}°C"


# ==============================================================================
# INTERMEDIATE EXERCISES
# ==============================================================================

# Exercise 6: Bank Account with Encapsulation
class BankAccount:
    """Bank account with encapsulated private data."""

    def __init__(self, account_number, owner, initial_balance=0):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print(f"Insufficient funds. Available: ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def get_balance(self):
        """Return current balance."""
        return self.__balance

    def transfer(self, amount, target_account):
        """Transfer money to another account."""
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.__balance:
            print(f"Insufficient funds for transfer. Available: ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            target_account.deposit(amount)
            print(f"Transferred ${amount:.2f} to {target_account.owner}")

    @property
    def owner(self):
        """Read-only owner property."""
        return self.__owner

    @property
    def account_number(self):
        """Read-only account number property."""
        return self.__account_number


# Exercise 7: Animal Inheritance
class Animal:
    """Base class for all animals."""

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        """Animal eating behavior."""
        print(f"{self.name} is eating.")

    def sleep(self):
        """Animal sleeping behavior."""
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        """Generic animal sound."""
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    """Dog that inherits from Animal."""

    def __init__(self, name, age):
        super().__init__(name, age, "Dog")

    def make_sound(self):
        """Override to bark."""
        print(f"{self.name} says: Woof! Woof!")


class Cat(Animal):
    """Cat that inherits from Animal."""

    def __init__(self, name, age):
        super().__init__(name, age, "Cat")

    def make_sound(self):
        """Override to meow."""
        print(f"{self.name} says: Meow!")


class Bird(Animal):
    """Bird that inherits from Animal."""

    def __init__(self, name, age):
        super().__init__(name, age, "Bird")

    def make_sound(self):
        """Override to chirp."""
        print(f"{self.name} says: Chirp chirp!")

    def fly(self):
        """Birds can fly."""
        print(f"{self.name} is flying!")


# Exercise 8: Shape Hierarchy
class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate circle area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate circle circumference."""
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


class RectangleShape(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Triangle(Shape):
    """Triangle shape."""

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """Calculate triangle area using Heron's formula."""
        s = self.perimeter() / 2  # semi-perimeter
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        """Calculate triangle perimeter."""
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Triangle(sides={self.side1}, {self.side2}, {self.side3})"


def total_area(shapes):
    """Calculate total area of a list of shapes."""
    return sum(shape.area() for shape in shapes)


# Exercise 9: Employee System
class Employee:
    """Base class for all employees."""

    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        """Calculate employee salary. Override in child classes."""
        return self.base_salary

    def display_info(self):
        """Display employee information."""
        print(f"\n--- Employee Info ---")
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: ${self.calculate_salary():.2f}")


class FullTimeEmployee(Employee):
    """Full-time employee with benefits."""

    def calculate_salary(self):
        """Full salary plus $500 benefits."""
        return self.base_salary + 500


class PartTimeEmployee(Employee):
    """Part-time employee paid by the hour."""

    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Calculate based on hours worked."""
        return self.hourly_rate * self.hours_worked


class Contractor(Employee):
    """Contractor paid by project."""

    def __init__(self, name, employee_id, project_fee):
        super().__init__(name, employee_id, 0)
        self.project_fee = project_fee

    def calculate_salary(self):
        """Return fixed project fee."""
        return self.project_fee


# Exercise 10: Shopping Cart
class Product:
    """Represents a product in inventory."""

    def __init__(self, name, price, quantity_available):
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def reduce_stock(self, amount):
        """Reduce available stock."""
        if amount <= self.quantity_available:
            self.quantity_available -= amount
            return True
        return False

    def display(self):
        """Display product information."""
        print(f"{self.name} - ${self.price:.2f} (Stock: {self.quantity_available})")


class CartItem:
    """Represents an item in the shopping cart."""

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_subtotal(self):
        """Calculate subtotal for this item."""
        return self.product.price * self.quantity


class ShoppingCart:
    """Shopping cart to manage customer purchases."""

    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        """Add item to cart with stock checking."""
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        if quantity > product.quantity_available:
            print(f"Not enough stock. Available: {product.quantity_available}")
            return

        # Check if product already in cart
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                print(f"Updated {product.name} quantity to {item.quantity}")
                return

        # Add new item
        self.items.append(CartItem(product, quantity))
        print(f"Added {quantity} x {product.name} to cart")

    def remove_item(self, product_name):
        """Remove item from cart."""
        self.items = [item for item in self.items if item.product.name != product_name]
        print(f"Removed {product_name} from cart")

    def get_total(self):
        """Calculate total cost."""
        return sum(item.get_subtotal() for item in self.items)

    def checkout(self):
        """Display cart and process checkout."""
        print("\n=== Shopping Cart ===")
        if not self.items:
            print("Cart is empty")
            return

        for item in self.items:
            print(f"{item.quantity} x {item.product.name} @ ${item.product.price:.2f} = ${item.get_subtotal():.2f}")

        print(f"\nTotal: ${self.get_total():.2f}")

        # Reduce stock for all items
        for item in self.items:
            item.product.reduce_stock(item.quantity)

        print("Checkout complete!")
        self.items = []


# ==============================================================================
# ADVANCED EXERCISES
# ==============================================================================

# Exercise 11: Library Management System
class LibraryBook:
    """Book in the library system."""

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_date = None


class Member:
    """Library member."""

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []


class Library:
    """Library management system."""

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"Added '{book.title}' to library")

    def add_member(self, member):
        """Add a member to the library."""
        self.members.append(member)
        print(f"Added member: {member.name}")

    def borrow_book(self, member_id, isbn):
        """Allow member to borrow a book."""
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print("Member not found")
            return

        book = next((b for b in self.books if b.isbn == isbn), None)
        if not book:
            print("Book not found")
            return

        if not book.is_available:
            print(f"'{book.title}' is not available")
            return

        book.is_available = False
        book.borrowed_date = datetime.now()
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member_id, isbn):
        """Process book return."""
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print("Member not found")
            return

        book = next((b for b in member.borrowed_books if b.isbn == isbn), None)
        if not book:
            print("Book not found in member's borrowed list")
            return

        # Calculate late fee
        days_borrowed = (datetime.now() - book.borrowed_date).days
        late_fee = max(0, (days_borrowed - 14) * 0.50)

        book.is_available = True
        book.borrowed_date = None
        member.borrowed_books.remove(book)

        print(f"{member.name} returned '{book.title}'")
        if late_fee > 0:
            print(f"Late fee: ${late_fee:.2f}")

    def search_books(self, query):
        """Search books by title or author."""
        results = [b for b in self.books if query.lower() in b.title.lower() or query.lower() in b.author.lower()]
        return results

    def display_member_books(self, member_id):
        """Display member's borrowed books."""
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print("Member not found")
            return

        print(f"\n{member.name}'s borrowed books:")
        for book in member.borrowed_books:
            print(f"- {book.title} by {book.author}")


# Exercise 12: Game Character System
class Inventory:
    """Character inventory system."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add item to inventory."""
        self.items.append(item)
        print(f"Added {item} to inventory")

    def remove_item(self, item):
        """Remove item from inventory."""
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from inventory")

    def display(self):
        """Display all items."""
        print(f"Inventory: {', '.join(self.items) if self.items else 'Empty'}")


class Character:
    """Base RPG character class."""

    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.inventory = Inventory()

    def take_damage(self, amount):
        """Take damage reduced by defense."""
        damage = max(0, amount - self.defense)
        self.health = max(0, self.health - damage)
        print(f"{self.name} took {damage} damage! Health: {self.health}/{self.max_health}")

    def attack(self, target):
        """Attack another character."""
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)

    def is_alive(self):
        """Check if character is alive."""
        return self.health > 0


class Warrior(Character):
    """Warrior class with high health and shield."""

    def __init__(self, name):
        super().__init__(name, health=150, attack_power=25, defense=10)
        self.shield_active = False

    def shield_block(self):
        """Activate shield for extra defense."""
        self.shield_active = True
        original_defense = self.defense
        self.defense += 15
        print(f"{self.name} raises shield! Defense: {original_defense} -> {self.defense}")


class Mage(Character):
    """Mage class with high attack and low health."""

    def __init__(self, name):
        super().__init__(name, health=80, attack_power=40, defense=3)

    def cast_spell(self, spell_name, target):
        """Cast a spell on target."""
        print(f"{self.name} casts {spell_name}!")
        damage = self.attack_power + 10
        target.take_damage(damage)


class Archer(Character):
    """Archer class with balanced stats."""

    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30, defense=5)

    def rapid_fire(self, target):
        """Shoot multiple arrows."""
        print(f"{self.name} uses Rapid Fire!")
        for i in range(3):
            target.take_damage(self.attack_power // 2)


# ==============================================================================
# CHALLENGE EXERCISES
# ==============================================================================

# Challenge 2: Refactored Student System
class StudentOOP:
    """OOP refactored student class with validation."""

    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        self._grades = []

    @property
    def name(self):
        """Get student name."""
        return self._name

    @property
    def student_id(self):
        """Get student ID."""
        return self._student_id

    @property
    def grades(self):
        """Get copy of grades."""
        return self._grades.copy()

    def add_grade(self, grade):
        """Add validated grade."""
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        self._grades.append(grade)

    def get_average(self):
        """Calculate average grade."""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)

    def __repr__(self):
        return f"StudentOOP(name='{self.name}', id='{self.student_id}', avg={self.get_average():.2f})"


# Challenge 3: Multiple Inheritance
class Fish:
    """Fish base class."""

    def __init__(self, name):
        self.name = name

    def swim(self):
        """Fish can swim."""
        print(f"{self.name} is swimming in water")


class FlyingCreature:
    """Flying creature base class."""

    def __init__(self, name):
        self.name = name

    def fly(self):
        """Can fly."""
        print(f"{self.name} is flying in the air")


class FlyingFish(Fish, FlyingCreature):
    """Flying fish using multiple inheritance."""

    def __init__(self, name):
        # Only call once to avoid diamond problem
        super().__init__(name)

    def glide(self):
        """Special ability unique to flying fish."""
        print(f"{self.name} is gliding above the water surface!")


# ==============================================================================
# DEMONSTRATION FUNCTIONS
# ==============================================================================

def demo_beginner_exercises():
    """Demonstrate beginner exercises."""
    print("\n" + "="*60)
    print("BEGINNER EXERCISES DEMO")
    print("="*60)

    # Exercise 1: Book
    print("\n--- Exercise 1: Book Class ---")
    book = Book("Python Basics", "John Smith", 350, 29.99, True)
    book.display_info()
    book.apply_discount(10)
    book.borrow()
    book.display_info()

    # Exercise 2: Rectangle
    print("\n--- Exercise 2: Rectangle Class ---")
    rect = Rectangle(5, 10)
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Is square? {rect.is_square()}")
    rect.scale(2)
    print(f"After scaling: {rect}")

    # Exercise 3: Student
    print("\n--- Exercise 3: Student Class ---")
    student = Student("Alice", "S001")
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(88)
    student.display_report_card()

    # Exercise 4: Counter
    print("\n--- Exercise 4: Counter Class ---")
    c1 = Counter()
    c2 = Counter()
    c1.increment()
    c1.increment()
    print(f"Counter 1: {c1.get_count()}")
    print(f"Total counters created: {Counter.get_total_counters()}")

    # Exercise 5: Temperature
    print("\n--- Exercise 5: Temperature Class ---")
    temp = Temperature(25)
    print(f"{temp} = {temp.to_fahrenheit():.1f}°F = {temp.to_kelvin():.1f}K")
    print(f"Is freezing? {Temperature.is_freezing(temp.celsius)}")


def demo_intermediate_exercises():
    """Demonstrate intermediate exercises."""
    print("\n" + "="*60)
    print("INTERMEDIATE EXERCISES DEMO")
    print("="*60)

    # Exercise 6: Bank Account
    print("\n--- Exercise 6: Bank Account ---")
    acc1 = BankAccount("ACC001", "Alice", 1000)
    acc2 = BankAccount("ACC002", "Bob", 500)
    acc1.deposit(200)
    acc1.withdraw(150)
    acc1.transfer(300, acc2)
    print(f"{acc1.owner}'s balance: ${acc1.get_balance():.2f}")
    print(f"{acc2.owner}'s balance: ${acc2.get_balance():.2f}")

    # Exercise 7: Animal Inheritance
    print("\n--- Exercise 7: Animal Inheritance ---")
    animals = [
        Dog("Buddy", 3),
        Cat("Whiskers", 2),
        Bird("Tweety", 1)
    ]
    for animal in animals:
        animal.make_sound()

    # Exercise 8: Shape Hierarchy
    print("\n--- Exercise 8: Shape Hierarchy ---")
    shapes = [
        Circle(5),
        RectangleShape(4, 6),
        Triangle(3, 4, 5)
    ]
    for shape in shapes:
        print(f"{shape}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
    print(f"Total area: {total_area(shapes):.2f}")

    # Exercise 9: Employee System
    print("\n--- Exercise 9: Employee System ---")
    employees = [
        FullTimeEmployee("Alice", "E001", 5000),
        PartTimeEmployee("Bob", "E002", 25, 80),
        Contractor("Charlie", "E003", 8000)
    ]
    for emp in employees:
        emp.display_info()


def demo_advanced_exercises():
    """Demonstrate advanced exercises."""
    print("\n" + "="*60)
    print("ADVANCED EXERCISES DEMO")
    print("="*60)

    # Exercise 10: Shopping Cart
    print("\n--- Exercise 10: Shopping Cart ---")
    laptop = Product("Laptop", 999.99, 5)
    mouse = Product("Mouse", 29.99, 10)
    cart = ShoppingCart()
    cart.add_item(laptop, 1)
    cart.add_item(mouse, 2)
    cart.checkout()

    # Exercise 12: Game Characters
    print("\n--- Exercise 12: Game Characters ---")
    warrior = Warrior("Conan")
    mage = Mage("Gandalf")
    print(f"\n{warrior.name} vs {mage.name}")
    warrior.shield_block()
    mage.cast_spell("Fireball", warrior)
    warrior.attack(mage)


if __name__ == "__main__":
    print("Python OOP Exercise Solutions")
    print("Run demo functions to see exercises in action:")
    print("- demo_beginner_exercises()")
    print("- demo_intermediate_exercises()")
    print("- demo_advanced_exercises()")

    # Uncomment to run demos
    # demo_beginner_exercises()
    # demo_intermediate_exercises()
    # demo_advanced_exercises()
