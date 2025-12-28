"""
Lesson 9: Class Methods and Static Methods in Python
=====================================================

Understanding different types of methods in Python classes:
- Instance methods: Operate on instance data (self)
- Class methods: Operate on class data (cls) using @classmethod
- Static methods: Utility functions related to class using @staticmethod

Key Concepts:
1. Instance methods vs class methods vs static methods
2. @classmethod decorator and alternative constructors
3. @staticmethod decorator and utility functions
4. Factory methods pattern
5. When to use each type
6. Class-level operations

Run this file: python lessons/09_class_methods.py
"""

from datetime import datetime, date


# =============================================================================
# 1. UNDERSTANDING THE THREE METHOD TYPES
# =============================================================================

class Employee:
    """Demonstrating all three method types."""

    company_name = "TechCorp"  # Class variable
    employee_count = 0         # Class variable

    def __init__(self, name, salary):
        """Instance method - takes 'self' as first parameter."""
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    # INSTANCE METHOD - operates on instance (self)
    def get_info(self):
        """
        Instance method: Has access to instance data via 'self'.
        Can access and modify instance attributes.
        """
        return f"{self.name} earns ${self.salary:,.2f}"

    def give_raise(self, amount):
        """Instance method: Modifies instance data."""
        self.salary += amount
        return f"{self.name} received a ${amount:,.2f} raise!"

    # CLASS METHOD - operates on class (cls)
    @classmethod
    def get_company_name(cls):
        """
        Class method: Has access to class data via 'cls'.
        Cannot access instance data (no 'self').
        Used for class-level operations.
        """
        return f"Company: {cls.company_name}"

    @classmethod
    def get_employee_count(cls):
        """Class method: Returns class-level data."""
        return f"Total employees: {cls.employee_count}"

    @classmethod
    def set_company_name(cls, name):
        """Class method: Modifies class-level data."""
        cls.company_name = name

    # STATIC METHOD - utility function
    @staticmethod
    def is_workday(day):
        """
        Static method: Doesn't access instance or class data.
        Takes no 'self' or 'cls' parameter.
        Just a utility function related to the class.
        """
        # 0 = Monday, 6 = Sunday
        return day.weekday() < 5


def demo_method_types():
    """Demonstrate the three method types."""
    print("\n" + "="*60)
    print("THREE METHOD TYPES")
    print("="*60)

    # Create instances
    emp1 = Employee("Alice", 75000)
    emp2 = Employee("Bob", 65000)

    print(f"\nINSTANCE METHODS (use 'self'):")
    print(f"  {emp1.get_info()}")
    print(f"  {emp2.get_info()}")
    print(f"  {emp1.give_raise(5000)}")
    print(f"  {emp1.get_info()}")

    print(f"\nCLASS METHODS (use 'cls'):")
    print(f"  {Employee.get_company_name()}")
    print(f"  {Employee.get_employee_count()}")
    # Can call on instance too (but uses class)
    print(f"  Via instance: {emp1.get_company_name()}")

    print(f"\nSTATIC METHODS (no 'self' or 'cls'):")
    today = date.today()
    print(f"  Today: {today.strftime('%A, %Y-%m-%d')}")
    print(f"  Is today a workday? {Employee.is_workday(today)}")
    # Can call on instance too
    print(f"  Via instance: {emp1.is_workday(today)}")


# =============================================================================
# 2. ALTERNATIVE CONSTRUCTORS WITH @classmethod
# =============================================================================

class Person:
    """Person class with alternative constructors."""

    def __init__(self, name, birth_year):
        """Standard constructor."""
        self.name = name
        self.birth_year = birth_year

    @classmethod
    def from_birth_date(cls, name, birth_date):
        """
        Alternative constructor: Create Person from birth date.
        Factory method pattern - creates and returns instance.
        """
        birth_year = birth_date.year
        return cls(name, birth_year)  # Calls __init__

    @classmethod
    def from_age(cls, name, age):
        """Alternative constructor: Create Person from current age."""
        current_year = datetime.now().year
        birth_year = current_year - age
        return cls(name, birth_year)

    @classmethod
    def from_string(cls, person_string):
        """
        Alternative constructor: Create Person from formatted string.
        Useful for parsing data from files, APIs, etc.
        """
        name, birth_year = person_string.split(',')
        return cls(name.strip(), int(birth_year.strip()))

    @property
    def age(self):
        """Calculate current age."""
        return datetime.now().year - self.birth_year

    def __str__(self):
        return f"{self.name} (born {self.birth_year}, age {self.age})"


def demo_alternative_constructors():
    """Demonstrate alternative constructors."""
    print("\n" + "="*60)
    print("ALTERNATIVE CONSTRUCTORS (@classmethod)")
    print("="*60)

    print(f"\nDifferent ways to create Person objects:\n")

    # Standard constructor
    person1 = Person("Alice", 1990)
    print(f"  Standard constructor:")
    print(f"    {person1}")

    # From birth date
    person2 = Person.from_birth_date("Bob", date(1985, 5, 15))
    print(f"\n  From birth date:")
    print(f"    {person2}")

    # From age
    person3 = Person.from_age("Charlie", 25)
    print(f"\n  From current age:")
    print(f"    {person3}")

    # From string
    person4 = Person.from_string("Diana, 1995")
    print(f"\n  From string:")
    print(f"    {person4}")


# =============================================================================
# 3. FACTORY METHODS PATTERN
# =============================================================================

class DatabaseConnection:
    """Database connection with factory methods."""

    def __init__(self, host, port, database, connection_type):
        self.host = host
        self.port = port
        self.database = database
        self.connection_type = connection_type

    @classmethod
    def mysql(cls, host, database):
        """Factory method for MySQL connection."""
        return cls(host, 3306, database, "MySQL")

    @classmethod
    def postgresql(cls, host, database):
        """Factory method for PostgreSQL connection."""
        return cls(host, 5432, database, "PostgreSQL")

    @classmethod
    def mongodb(cls, host, database):
        """Factory method for MongoDB connection."""
        return cls(host, 27017, database, "MongoDB")

    @classmethod
    def sqlite(cls, database_file):
        """Factory method for SQLite connection (file-based)."""
        return cls("localhost", 0, database_file, "SQLite")

    def __str__(self):
        if self.connection_type == "SQLite":
            return f"{self.connection_type} connection to {self.database}"
        return f"{self.connection_type} connection to {self.database} at {self.host}:{self.port}"


def demo_factory_methods():
    """Demonstrate factory methods pattern."""
    print("\n" + "="*60)
    print("FACTORY METHODS PATTERN")
    print("="*60)

    print(f"\nCreating database connections using factory methods:\n")

    # Clean, readable way to create different connection types
    mysql_conn = DatabaseConnection.mysql("localhost", "users_db")
    postgres_conn = DatabaseConnection.postgresql("localhost", "products_db")
    mongo_conn = DatabaseConnection.mongodb("localhost", "logs_db")
    sqlite_conn = DatabaseConnection.sqlite("local.db")

    connections = [mysql_conn, postgres_conn, mongo_conn, sqlite_conn]

    for conn in connections:
        print(f"  {conn}")


# =============================================================================
# 4. STATIC METHODS AS UTILITIES
# =============================================================================

class MathUtils:
    """Collection of math utility functions."""

    @staticmethod
    def is_prime(n):
        """
        Check if number is prime.
        Static method: Doesn't need instance or class data.
        Just a utility function grouped with the class.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        """Calculate factorial."""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def fibonacci(n):
        """Generate Fibonacci sequence up to n terms."""
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib


class StringUtils:
    """String utility functions."""

    @staticmethod
    def reverse(text):
        """Reverse a string."""
        return text[::-1]

    @staticmethod
    def is_palindrome(text):
        """Check if string is palindrome."""
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def word_count(text):
        """Count words in text."""
        return len(text.split())

    @staticmethod
    def title_case(text):
        """Convert to title case."""
        return ' '.join(word.capitalize() for word in text.split())


def demo_static_utilities():
    """Demonstrate static methods as utilities."""
    print("\n" + "="*60)
    print("STATIC METHODS AS UTILITIES")
    print("="*60)

    print(f"\nMath Utilities:")
    print(f"  Is 17 prime? {MathUtils.is_prime(17)}")
    print(f"  Is 20 prime? {MathUtils.is_prime(20)}")
    print(f"  Factorial of 5: {MathUtils.factorial(5)}")
    print(f"  First 10 Fibonacci numbers: {MathUtils.fibonacci(10)}")

    print(f"\nString Utilities:")
    text = "A man a plan a canal Panama"
    print(f"  Original: '{text}'")
    print(f"  Reversed: '{StringUtils.reverse(text)}'")
    print(f"  Is palindrome? {StringUtils.is_palindrome(text)}")
    print(f"  Word count: {StringUtils.word_count(text)}")
    print(f"  Title case: '{StringUtils.title_case('hello world from python')}'")


# =============================================================================
# 5. WHEN TO USE EACH METHOD TYPE
# =============================================================================

class Product:
    """Product class demonstrating when to use each method type."""

    tax_rate = 0.08  # Class variable

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # INSTANCE METHOD: Works with instance data
    def total_price(self):
        """Calculate total price for this product."""
        return self.price * self.quantity

    def total_with_tax(self):
        """Calculate total with tax using class tax rate."""
        return self.total_price() * (1 + Product.tax_rate)

    # CLASS METHOD: Works with class data or creates instances
    @classmethod
    def set_tax_rate(cls, rate):
        """Modify class-level tax rate for all products."""
        cls.tax_rate = rate

    @classmethod
    def from_dict(cls, data):
        """Alternative constructor from dictionary."""
        return cls(data['name'], data['price'], data['quantity'])

    # STATIC METHOD: Utility function related to products
    @staticmethod
    def validate_price(price):
        """Validate if price is acceptable."""
        return isinstance(price, (int, float)) and price > 0

    @staticmethod
    def format_currency(amount):
        """Format amount as currency."""
        return f"${amount:,.2f}"

    def __str__(self):
        return f"{self.name}: {self.quantity} @ ${self.price:.2f} = ${self.total_price():.2f}"


def demo_when_to_use_each():
    """Demonstrate when to use each method type."""
    print("\n" + "="*60)
    print("WHEN TO USE EACH METHOD TYPE")
    print("="*60)

    product = Product("Laptop", 999.99, 2)

    print(f"\nINSTANCE METHOD - Use when:")
    print(f"  - You need to access or modify instance data")
    print(f"  - Operation is specific to one instance")
    print(f"  Example: {product.total_price()}")
    print(f"  Example: {Product.format_currency(product.total_with_tax())}")

    print(f"\nCLASS METHOD - Use when:")
    print(f"  - You need to access or modify class data")
    print(f"  - Creating alternative constructors (factory methods)")
    print(f"  - Operation affects all instances")
    print(f"  Example: Setting tax rate for all products")
    Product.set_tax_rate(0.10)
    print(f"  New tax rate: {Product.tax_rate}")

    data = {'name': 'Mouse', 'price': 29.99, 'quantity': 5}
    product2 = Product.from_dict(data)
    print(f"  Created from dict: {product2}")

    print(f"\nSTATIC METHOD - Use when:")
    print(f"  - Function doesn't need instance or class data")
    print(f"  - Utility function logically related to the class")
    print(f"  - Could be a standalone function but grouped for organization")
    print(f"  Example: Validate price: {Product.validate_price(50)}")
    print(f"  Example: Validate price: {Product.validate_price(-10)}")


# =============================================================================
# 6. REAL-WORLD EXAMPLE: User Management System
# =============================================================================

class User:
    """User management system with all method types."""

    # Class variables
    all_users = []
    next_id = 1
    password_min_length = 8

    def __init__(self, username, email, password):
        """Instance method: Create new user."""
        if not self.validate_username(username):
            raise ValueError("Invalid username")
        if not self.validate_email(email):
            raise ValueError("Invalid email")
        if not self.validate_password(password):
            raise ValueError(f"Password must be at least {User.password_min_length} characters")

        self.id = User.next_id
        User.next_id += 1
        self.username = username
        self.email = email
        self._password = self._hash_password(password)
        self.created_at = datetime.now()
        User.all_users.append(self)

    # INSTANCE METHODS: Work with instance data
    def update_email(self, new_email):
        """Update user email."""
        if not self.validate_email(new_email):
            raise ValueError("Invalid email")
        self.email = new_email

    def check_password(self, password):
        """Check if password matches."""
        return self._hash_password(password) == self._password

    def get_account_age_days(self):
        """Get account age in days."""
        return (datetime.now() - self.created_at).days

    # CLASS METHODS: Work with class data or create instances
    @classmethod
    def find_by_username(cls, username):
        """Find user by username."""
        for user in cls.all_users:
            if user.username == username:
                return user
        return None

    @classmethod
    def find_by_id(cls, user_id):
        """Find user by ID."""
        for user in cls.all_users:
            if user.id == user_id:
                return user
        return None

    @classmethod
    def get_user_count(cls):
        """Get total number of users."""
        return len(cls.all_users)

    @classmethod
    def set_password_policy(cls, min_length):
        """Update password policy for all users."""
        cls.password_min_length = min_length

    @classmethod
    def from_registration_form(cls, form_data):
        """Alternative constructor from registration form."""
        return cls(
            form_data.get('username'),
            form_data.get('email'),
            form_data.get('password')
        )

    # STATIC METHODS: Utility functions
    @staticmethod
    def validate_username(username):
        """Validate username format."""
        return (isinstance(username, str) and
                3 <= len(username) <= 20 and
                username.isalnum())

    @staticmethod
    def validate_email(email):
        """Validate email format."""
        return isinstance(email, str) and '@' in email and '.' in email

    @staticmethod
    def validate_password(password):
        """Validate password strength."""
        return (isinstance(password, str) and
                len(password) >= User.password_min_length)

    @staticmethod
    def _hash_password(password):
        """Hash password (simplified for demo)."""
        return f"hashed_{password}"

    def __str__(self):
        return f"User #{self.id}: {self.username} ({self.email})"

    def __repr__(self):
        return f"User(id={self.id}, username={self.username!r})"


def demo_user_management():
    """Demonstrate comprehensive method usage."""
    print("\n" + "="*60)
    print("REAL-WORLD EXAMPLE: User Management System")
    print("="*60)

    # Create users using different methods
    print(f"\nCreating users:")
    user1 = User("alice123", "alice@example.com", "password123")
    print(f"  {user1}")

    user2 = User("bob456", "bob@example.com", "securepass456")
    print(f"  {user2}")

    # Alternative constructor
    form_data = {
        'username': 'charlie',
        'email': 'charlie@example.com',
        'password': 'charlie789'
    }
    user3 = User.from_registration_form(form_data)
    print(f"  {user3}")

    # Instance methods
    print(f"\nInstance operations:")
    print(f"  User1 account age: {user1.get_account_age_days()} days")
    print(f"  Checking password: {user1.check_password('password123')}")
    user1.update_email("alice.new@example.com")
    print(f"  Updated email: {user1.email}")

    # Class methods
    print(f"\nClass operations:")
    print(f"  Total users: {User.get_user_count()}")
    found_user = User.find_by_username("bob456")
    print(f"  Found by username: {found_user}")
    found_by_id = User.find_by_id(2)
    print(f"  Found by ID: {found_by_id}")

    # Static methods
    print(f"\nStatic utility validations:")
    print(f"  Valid username 'test123': {User.validate_username('test123')}")
    print(f"  Valid username 'ab': {User.validate_username('ab')}")  # Too short
    print(f"  Valid email 'test@test.com': {User.validate_email('test@test.com')}")
    print(f"  Valid password 'short': {User.validate_password('short')}")  # Too short


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

def print_key_takeaways():
    """Print key learning points."""
    print("\n" + "="*60)
    print("KEY TAKEAWAYS - Class Methods and Static Methods")
    print("="*60)

    takeaways = [
        "1. INSTANCE METHODS: Use 'self', work with instance data",
        "2. CLASS METHODS: Use 'cls', work with class data",
        "3. STATIC METHODS: No 'self' or 'cls', utility functions",
        "",
        "4. @classmethod - Perfect for:",
        "   - Alternative constructors (factory methods)",
        "   - Modifying class-level data",
        "   - Operations affecting all instances",
        "",
        "5. @staticmethod - Perfect for:",
        "   - Utility functions related to the class",
        "   - Validation functions",
        "   - Helper functions that don't need instance/class data",
        "",
        "6. Factory methods provide clean, readable object creation",
        "7. Class methods can access and modify class variables",
        "8. Static methods are like standalone functions but grouped logically",
        "9. All three types can be called on class or instance",
        "10. Choose based on what data the method needs to access"
    ]

    for takeaway in takeaways:
        print(f"  {takeaway}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*60)
    print("LESSON 9: CLASS METHODS AND STATIC METHODS")
    print("="*60)

    # Run all demonstrations
    demo_method_types()
    demo_alternative_constructors()
    demo_factory_methods()
    demo_static_utilities()
    demo_when_to_use_each()
    demo_user_management()
    print_key_takeaways()

    print("\n" + "="*60)
    print("LESSON COMPLETE!")
    print("="*60)
    print("\nNext: Lesson 10 - Advanced OOP Concepts")
    print("Run: python lessons/10_advanced_oop.py")
