"""
LESSON 2: ATTRIBUTES AND METHODS
=================================

Deep dive into attributes and methods in Python OOP.

Key Concepts:
- Instance vs Class attributes
- Instance vs Class methods
- Static methods
- Method types
- Attribute access
"""

print("="*70)
print("LESSON 2: ATTRIBUTES AND METHODS")
print("="*70)

# ============================================================================
# INSTANCE ATTRIBUTES vs CLASS ATTRIBUTES
# ============================================================================

print("\n### Example 1: Instance vs Class Attributes ###\n")

class Dog:
    """Demonstrating instance and class attributes"""

    # CLASS ATTRIBUTE - shared by ALL instances
    species = "Canis familiaris"
    total_dogs = 0

    def __init__(self, name, age):
        # INSTANCE ATTRIBUTES - unique to each instance
        self.name = name
        self.age = age

        # Increment class attribute
        Dog.total_dogs += 1

# Create dogs
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
dog3 = Dog("Charlie", 2)

print(f"{dog1.name}: species = {dog1.species}, age = {dog1.age}")
print(f"{dog2.name}: species = {dog2.species}, age = {dog2.age}")

# Class attribute is same for all
print(f"\nAll dogs are: {Dog.species}")
print(f"Total dogs created: {Dog.total_dogs}")

# Changing class attribute affects all instances
Dog.species = "Canis lupus familiaris"
print(f"\nAfter changing class attribute:")
print(f"{dog1.name}'s species: {dog1.species}")
print(f"{dog2.name}'s species: {dog2.species}")

# But changing instance attribute only affects that instance
dog1.name = "Buddy Jr."
print(f"\nAfter changing instance attribute:")
print(f"dog1 name: {dog1.name}")
print(f"dog2 name: {dog2.name}")  # Unchanged


# ============================================================================
# INSTANCE METHODS
# ============================================================================

print("\n### Example 2: Instance Methods ###\n")

class Circle:
    """Circle with instance methods"""

    PI = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    # INSTANCE METHOD - operates on instance data
    def area(self):
        """Calculate area - uses instance attribute (self.radius)"""
        return Circle.PI * self.radius ** 2

    def circumference(self):
        """Calculate circumference"""
        return 2 * Circle.PI * self.radius

    def scale(self, factor):
        """Scale the circle by a factor"""
        self.radius *= factor
        print(f"Circle scaled by {factor}. New radius: {self.radius}")

# Create circles
circle1 = Circle(5)
circle2 = Circle(10)

print(f"Circle 1: radius={circle1.radius}, area={circle1.area():.2f}")
print(f"Circle 2: radius={circle2.radius}, area={circle2.area():.2f}")

circle1.scale(2)
print(f"Circle 1 after scaling: area={circle1.area():.2f}")


# ============================================================================
# CLASS METHODS
# ============================================================================

print("\n### Example 3: Class Methods ###\n")

class Employee:
    """Employee with class methods"""

    # Class attributes
    company_name = "Tech Corp"
    total_employees = 0
    raise_amount = 1.04  # 4% raise

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    # INSTANCE METHOD
    def apply_raise(self):
        """Apply raise to this employee"""
        self.salary = int(self.salary * Employee.raise_amount)

    # CLASS METHOD - operates on class data
    @classmethod
    def set_raise_amount(cls, amount):
        """
        Set raise amount for ALL employees

        cls = reference to the CLASS (like self for instances)
        """
        cls.raise_amount = amount
        print(f"Raise amount changed to {amount}")

    @classmethod
    def from_string(cls, emp_string):
        """
        Alternative constructor - create employee from string

        cls lets us create new instances
        """
        name, salary = emp_string.split('-')
        return cls(name, int(salary))

    @classmethod
    def get_employee_count(cls):
        """Get total number of employees"""
        return cls.total_employees

    def display_info(self):
        print(f"{self.name}: ${self.salary:,}")

# Create employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print("Before raise:")
emp1.display_info()
emp2.display_info()

# Apply raise to individual
emp1.apply_raise()
print("\nAfter Alice's raise:")
emp1.display_info()

# Change raise amount for ALL employees (class method)
Employee.set_raise_amount(1.10)  # 10% raise
emp2.apply_raise()
print("\nAfter changing company raise amount and Bob's raise:")
emp2.display_info()

# Alternative constructor (class method)
emp3 = Employee.from_string("Charlie-70000")
print(f"\nEmployee created from string:")
emp3.display_info()

# Get employee count (class method)
print(f"\nTotal employees: {Employee.get_employee_count()}")


# ============================================================================
# STATIC METHODS
# ============================================================================

print("\n### Example 4: Static Methods ###\n")

class MathOperations:
    """Utility class with static methods"""

    # STATIC METHOD - doesn't access instance or class data
    @staticmethod
    def add(x, y):
        """Add two numbers - no self or cls needed"""
        return x + y

    @staticmethod
    def is_even(num):
        """Check if number is even"""
        return num % 2 == 0

    @staticmethod
    def factorial(n):
        """Calculate factorial"""
        if n <= 1:
            return 1
        return n * MathOperations.factorial(n - 1)

# Use static methods - don't need to create instance
print(f"5 + 3 = {MathOperations.add(5, 3)}")
print(f"Is 10 even? {MathOperations.is_even(10)}")
print(f"5! = {MathOperations.factorial(5)}")

# Can also call from instance (but unusual)
math = MathOperations()
print(f"7 + 2 = {math.add(7, 2)}")


# ============================================================================
# COMPARISON: Instance vs Class vs Static Methods
# ============================================================================

print("\n### Example 5: Method Types Comparison ###\n")

class Pizza:
    """Demonstrating all three method types"""

    # Class attribute
    total_pizzas = 0

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        Pizza.total_pizzas += 1

    # INSTANCE METHOD - uses 'self', accesses instance data
    def describe(self):
        """Describe THIS specific pizza"""
        return f"{self.size} pizza with {', '.join(self.toppings)}"

    def add_topping(self, topping):
        """Add topping to THIS pizza"""
        self.toppings.append(topping)

    # CLASS METHOD - uses 'cls', accesses class data
    @classmethod
    def margherita(cls):
        """Create a margherita pizza (alternative constructor)"""
        return cls("Medium", ["Cheese", "Tomato", "Basil"])

    @classmethod
    def get_total_pizzas(cls):
        """Get total pizzas made"""
        return cls.total_pizzas

    # STATIC METHOD - uses neither 'self' nor 'cls'
    @staticmethod
    def is_valid_size(size):
        """Check if pizza size is valid"""
        return size in ["Small", "Medium", "Large", "Extra Large"]

    @staticmethod
    def mix_sauce(ingredient1, ingredient2):
        """Mix pizza sauce - no instance/class data needed"""
        return f"Sauce made from {ingredient1} and {ingredient2}"

# Instance method - need an instance
pizza1 = Pizza("Large", ["Pepperoni", "Mushrooms"])
print(f"Instance method: {pizza1.describe()}")
pizza1.add_topping("Olives")
print(f"After adding topping: {pizza1.describe()}")

# Class method - can call on class itself
pizza2 = Pizza.margherita()
print(f"\nClass method (alt constructor): {pizza2.describe()}")
print(f"Total pizzas: {Pizza.get_total_pizzas()}")

# Static method - can call on class, doesn't need instance
print(f"\nStatic method: Is 'Jumbo' valid? {Pizza.is_valid_size('Jumbo')}")
print(f"Static method: Is 'Large' valid? {Pizza.is_valid_size('Large')}")
print(f"Static method: {Pizza.mix_sauce('Tomato', 'Garlic')}")


# ============================================================================
# PRIVATE ATTRIBUTES AND METHODS
# ============================================================================

print("\n### Example 6: Private Attributes/Methods ###\n")

class BankAccount:
    """Bank account with private attributes"""

    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self._account_number = None  # Protected (single underscore)
        self.__balance = balance     # Private (double underscore)

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__log_transaction("Deposit", amount)

    def withdraw(self, amount):
        if self.__is_valid_withdrawal(amount):
            self.__balance -= amount
            self.__log_transaction("Withdrawal", amount)
        else:
            print("Invalid withdrawal!")

    def get_balance(self):
        """Public method to access private balance"""
        return self.__balance

    # Private method (double underscore)
    def __is_valid_withdrawal(self, amount):
        """Private helper method"""
        return 0 < amount <= self.__balance

    def __log_transaction(self, trans_type, amount):
        """Private method to log transactions"""
        print(f"[LOG] {trans_type}: ${amount:.2f}, Balance: ${self.__balance:.2f}")

# Create account
account = BankAccount("John", 1000)

# Public method works
print(f"Owner: {account.owner}")  # Public attribute - OK
print(f"Balance: ${account.get_balance():.2f}")  # Public method - OK

account.deposit(500)
account.withdraw(200)

# Can't access private attributes directly (name mangling)
# print(account.__balance)  # Would raise AttributeError

# But can still access with name mangling (not recommended!)
print(f"\nAccessing 'private' balance (not recommended): ${account._BankAccount__balance:.2f}")


# ============================================================================
# REAL-WORLD EXAMPLE: Product Inventory
# ============================================================================

print("\n### Example 7: Product Inventory System ###\n")

class Product:
    """Product in inventory system"""

    # Class attributes
    total_products = 0
    low_stock_threshold = 10

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.total_products += 1

    # Instance methods
    def restock(self, amount):
        """Add stock"""
        self.quantity += amount
        print(f"Restocked {amount} units of {self.name}")

    def sell(self, amount):
        """Sell products"""
        if amount <= self.quantity:
            self.quantity -= amount
            revenue = amount * self.price
            print(f"Sold {amount} units of {self.name}. Revenue: ${revenue:.2f}")
            if self.is_low_stock():
                print(f"⚠️  WARNING: {self.name} is low on stock!")
            return revenue
        else:
            print(f"Not enough stock! Only {self.quantity} units available")
            return 0

    def is_low_stock(self):
        """Check if product is low on stock"""
        return self.quantity < Product.low_stock_threshold

    def get_value(self):
        """Get total value of stock"""
        return self.quantity * self.price

    # Class method
    @classmethod
    def set_low_stock_threshold(cls, threshold):
        """Set low stock threshold for all products"""
        cls.low_stock_threshold = threshold

    # Static method
    @staticmethod
    def calculate_discount(price, discount_percent):
        """Calculate discounted price"""
        return price * (1 - discount_percent / 100)

    def display_info(self):
        """Display product information"""
        status = "LOW STOCK" if self.is_low_stock() else "In Stock"
        print(f"\n{self.name} (ID: {self.product_id})")
        print(f"  Price: ${self.price:.2f}")
        print(f"  Quantity: {self.quantity} [{status}]")
        print(f"  Stock Value: ${self.get_value():.2f}")

# Create products
laptop = Product("P001", "Laptop", 999.99, 25)
mouse = Product("P002", "Mouse", 29.99, 8)
keyboard = Product("P003", "Keyboard", 79.99, 50)

# Use instance methods
laptop.display_info()
laptop.sell(10)
laptop.display_info()

mouse.display_info()
mouse.restock(20)
mouse.display_info()

# Use static method
sale_price = Product.calculate_discount(laptop.price, 15)
print(f"\nLaptop sale price (15% off): ${sale_price:.2f}")

# Use class method
print(f"\nTotal products in system: {Product.total_products}")


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "="*70)
print("KEY TAKEAWAYS:")
print("="*70)
print("""
ATTRIBUTES:
-----------
1. INSTANCE ATTRIBUTES (self.x)
   - Unique to each object
   - Created in __init__
   - Access with self.attribute_name

2. CLASS ATTRIBUTES (ClassName.x)
   - Shared by all instances
   - Defined in class body
   - Access with ClassName.attribute_name or cls.attribute_name

METHODS:
--------
1. INSTANCE METHODS (def method(self):)
   - Take 'self' as first parameter
   - Can access instance and class attributes
   - Called on instances: obj.method()

2. CLASS METHODS (@classmethod def method(cls):)
   - Take 'cls' as first parameter
   - Can't access instance attributes
   - Called on class: ClassName.method()
   - Use for alternative constructors

3. STATIC METHODS (@staticmethod def method():)
   - No self or cls parameter
   - Can't access instance or class attributes
   - Called on class: ClassName.method()
   - Use for utility functions

PRIVACY:
--------
- Public: attribute (no underscore)
- Protected: _attribute (single underscore) - convention only
- Private: __attribute (double underscore) - name mangling
""")


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES:")
print("="*70)
print("""
1. Create a 'Counter' class with:
   - Class attribute: total_counters
   - Instance attribute: count
   - Instance methods: increment(), decrement(), reset()
   - Class method: get_total_counters()

2. Create a 'Temperature' class with:
   - Instance attribute: celsius
   - Instance method: to_fahrenheit()
   - Class method: from_fahrenheit(f) - returns Temperature object
   - Static method: is_freezing(celsius)

3. Create a 'Player' class (game) with:
   - Class attribute: total_players
   - Instance attributes: name, score, lives
   - Instance methods: add_score(), lose_life(), is_alive()
   - Class method: from_save_file(save_string)
   - Static method: validate_name(name)

4. Create a 'Library' class with:
   - Class attribute: total_books
   - Instance attributes: title, author, isbn, __is_available
   - Instance methods: borrow(), return_book(), get_status()
   - Private method: __log_transaction()

5. Create a 'Config' class with:
   - Multiple class attributes (settings)
   - Class methods to get/set configuration
   - Static methods for validation
   - No instance methods (configuration utility class)
""")


if __name__ == "__main__":
    print("\nLesson 2 Complete! ✓")
    print("Next: Run lessons/03_encapsulation.py")
