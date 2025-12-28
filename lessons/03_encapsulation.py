"""
LESSON 3: ENCAPSULATION
========================

First Pillar of OOP: Bundling data and methods, hiding internal details.

Key Concepts:
- Data hiding
- Getters and setters
- Property decorators
- Access control
- Information hiding
"""

print("="*70)
print("LESSON 3: ENCAPSULATION")
print("="*70)

# ============================================================================
# WHAT IS ENCAPSULATION?
# ============================================================================
# Encapsulation = Bundling data (attributes) and methods that operate on
# that data into a single unit (class), and hiding the internal details.
#
# Benefits:
# 1. Data protection - prevent invalid data
# 2. Flexibility - change implementation without affecting users
# 3. Maintainability - easier to modify and debug

# ============================================================================
# EXAMPLE 1: Without Encapsulation (Bad)
# ============================================================================

print("\n### Example 1: Without Encapsulation (Problems) ###\n")

class BankAccount_Bad:
    def __init__(self, balance):
        self.balance = balance  # Public - anyone can modify!

# Problem: Direct access allows invalid operations
account = BankAccount_Bad(1000)
print(f"Initial balance: ${account.balance}")

# Bad! Can set negative balance
account.balance = -500
print(f"After direct modification: ${account.balance}")  # Invalid!

# Bad! No validation or logging
account.balance += 1000000  # Who made this deposit?
print(f"Suspicious balance: ${account.balance}")


# ============================================================================
# EXAMPLE 2: With Encapsulation (Good)
# ============================================================================

print("\n### Example 2: With Encapsulation (Better) ###\n")

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance  # Private attribute
        self.__transaction_history = []

    def deposit(self, amount):
        """Controlled access with validation"""
        if amount > 0:
            self.__balance += amount
            self.__log_transaction("Deposit", amount)
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Controlled access with validation"""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.__balance:
            print(f"Insufficient funds! Balance: ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            self.__log_transaction("Withdrawal", amount)
            print(f"Withdrew ${amount:.2f}")

    def get_balance(self):
        """Getter - controlled read access"""
        return self.__balance

    def get_transaction_history(self):
        """Getter for transaction history"""
        return self.__transaction_history.copy()  # Return copy, not original

    def __log_transaction(self, trans_type, amount):
        """Private method - internal implementation"""
        self.__transaction_history.append({
            'type': trans_type,
            'amount': amount,
            'balance': self.__balance
        })

# Now the balance is protected
account = BankAccount("ACC001", 1000)
print(f"Initial balance: ${account.get_balance():.2f}")

# Must use methods - validation is enforced
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Blocked - insufficient funds

# Can't directly modify balance
# account.__balance = -500  # Won't work (name mangling)

print(f"\nFinal balance: ${account.get_balance():.2f}")
print(f"Transactions: {len(account.get_transaction_history())}")


# ============================================================================
# EXAMPLE 3: Getters and Setters
# ============================================================================

print("\n### Example 3: Getters and Setters ###\n")

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter methods
    def get_name(self):
        """Get person's name"""
        return self.__name

    def get_age(self):
        """Get person's age"""
        return self.__age

    # Setter methods with validation
    def set_name(self, name):
        """Set person's name with validation"""
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name!")

    def set_age(self, age):
        """Set person's age with validation"""
        if isinstance(age, int) and 0 <= age <= 150:
            self.__age = age
        else:
            print("Invalid age! Must be between 0 and 150")

# Use getters and setters
person = Person("Alice", 25)
print(f"Name: {person.get_name()}, Age: {person.get_age()}")

# Setters validate input
person.set_age(30)
print(f"After valid age change: {person.get_age()}")

person.set_age(-5)  # Invalid - rejected
person.set_age(200)  # Invalid - rejected
print(f"Age remains: {person.get_age()}")


# ============================================================================
# EXAMPLE 4: Property Decorators (Pythonic Way)
# ============================================================================

print("\n### Example 4: Property Decorators ###\n")

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # PROPERTY - acts like attribute but has validation
    @property
    def name(self):
        """Getter for name"""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter for name with validation"""
        if isinstance(value, str) and len(value) > 0:
            self.__name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def salary(self):
        """Getter for salary"""
        return self.__salary

    @salary.setter
    def salary(self, value):
        """Setter for salary with validation"""
        if isinstance(value, (int, float)) and value >= 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be non-negative number")

    @property
    def annual_salary(self):
        """Read-only property (no setter)"""
        return self.__salary * 12

    @property
    def formatted_salary(self):
        """Computed property"""
        return f"${self.__salary:,.2f}"

# Use properties like attributes (but with validation)
emp = Employee("Bob", 5000)
print(f"Name: {emp.name}")  # Calls getter
print(f"Monthly: {emp.formatted_salary}")
print(f"Annual: ${emp.annual_salary:,.2f}")

# Setter is called automatically
emp.salary = 6000  # Calls setter with validation
print(f"New salary: {emp.formatted_salary}")

# Validation works
try:
    emp.salary = -1000  # Invalid
except ValueError as e:
    print(f"Error: {e}")

# Read-only property can't be set
try:
    emp.annual_salary = 100000
except AttributeError:
    print("Can't set read-only property")


# ============================================================================
# EXAMPLE 5: Real-World Example - Product Class
# ============================================================================

print("\n### Example 5: Product with Encapsulation ###\n")

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def product_id(self):
        """Read-only product ID"""
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self.__name = value
        else:
            raise ValueError("Invalid product name")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("Price must be positive")

    @property
    def quantity(self):
        return self.__quantity

    @property
    def total_value(self):
        """Computed property - read-only"""
        return self.__price * self.__quantity

    def add_stock(self, amount):
        """Add stock with validation"""
        if amount > 0:
            self.__quantity += amount
            print(f"Added {amount} units. New quantity: {self.__quantity}")
        else:
            print("Amount must be positive")

    def remove_stock(self, amount):
        """Remove stock with validation"""
        if amount <= 0:
            print("Amount must be positive")
        elif amount > self.__quantity:
            print(f"Not enough stock! Available: {self.__quantity}")
        else:
            self.__quantity -= amount
            print(f"Removed {amount} units. Remaining: {self.__quantity}")

# Create product
product = Product("P001", "Laptop", 999.99, 50)
print(f"Product: {product.name}")
print(f"Price: ${product.price:.2f}")
print(f"Stock: {product.quantity}")
print(f"Total Value: ${product.total_value:,.2f}")

# Controlled modifications
product.price = 899.99  # OK - uses setter
product.add_stock(10)   # OK - uses method
product.remove_stock(5) # OK - uses method

# Protected from invalid operations
try:
    product.price = -100  # Rejected by setter
except ValueError as e:
    print(f"Error: {e}")

# Can't modify product_id (read-only)
try:
    product.product_id = "P999"
except AttributeError:
    print("Can't modify product ID")


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "="*70)
print("KEY TAKEAWAYS:")
print("="*70)
print("""
ENCAPSULATION = Bundling data + methods, hiding implementation

BENEFITS:
1. Data Protection - validate inputs
2. Flexibility - change implementation without breaking code
3. Maintainability - easier to debug and modify

PRIVACY CONVENTIONS:
- public_attr     - Public, direct access
- _protected_attr - Protected, convention (don't use outside class/subclass)
- __private_attr  - Private, name mangling (don't use outside class)

GETTERS/SETTERS:
Old way:
    def get_value(self): return self.__value
    def set_value(self, val): self.__value = val

PROPERTY DECORATORS (Pythonic):
    @property
    def value(self): return self.__value

    @value.setter
    def value(self, val): self.__value = val

WHEN TO USE:
- Use encapsulation when data needs validation
- Use properties for computed values
- Use private attributes for implementation details
- Use public methods for interface

REMEMBER:
- Encapsulation != just making things private
- It's about providing controlled access with validation
- Protects object integrity
""")

print("\nLesson 3 Complete! ✓")
print("Next: Run lessons/04_inheritance.py")
