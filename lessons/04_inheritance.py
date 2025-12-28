"""
LESSON 4: INHERITANCE
=====================

Second Pillar of OOP: Creating new classes based on existing ones.

Key Concepts:
- Parent (base/super) class
- Child (derived/sub) class
- Inheriting attributes and methods
- Method overriding
- super() function
- Multiple inheritance
"""

print("="*70)
print("LESSON 4: INHERITANCE")
print("="*70)

# ============================================================================
# WHAT IS INHERITANCE?
# ============================================================================
# Inheritance allows a class to inherit attributes and methods from another
# class, promoting code reuse and creating hierarchical relationships.
#
# Parent Class (Base/Super class) - class being inherited from
# Child Class (Derived/Sub class) - class that inherits

# ============================================================================
# EXAMPLE 1: Basic Inheritance
# ============================================================================

print("\n### Example 1: Basic Inheritance ###\n")

class Animal:
    """Parent class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes a sound")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):  # Dog inherits from Animal
    """Child class"""

    def make_sound(self):  # Override parent method
        print(f"{self.name} says: Woof!")

class Cat(Animal):  # Cat also inherits from Animal
    """Child class"""

    def make_sound(self):  # Override parent method
        print(f"{self.name} says: Meow!")

# Create objects
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

# Inherited attributes
print(f"Dog: {dog.name}, {dog.age} years old")
print(f"Cat: {cat.name}, {cat.age} years old")

# Overridden methods
dog.make_sound()  # Uses Dog's version
cat.make_sound()  # Uses Cat's version

# Inherited methods
dog.sleep()  # Uses Animal's version
cat.sleep()  # Uses Animal's version


# ============================================================================
# EXAMPLE 2: Using super()
# ============================================================================

print("\n### Example 2: Using super() ###\n")

class Vehicle:
    """Parent class"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print(f"Vehicle created: {brand} {model}")

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping...")

class Car(Vehicle):
    """Child class"""

    def __init__(self, brand, model, year, num_doors):
        # Call parent constructor
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        print(f"Car has {num_doors} doors")

    def honk(self):
        print(f"{self.brand} {self.model}: Beep beep!")

class Motorcycle(Vehicle):
    """Another child class"""

    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        print(f"{self.brand} {self.model} does a wheelie!")

# Create vehicles
car = Car("Toyota", "Camry", 2023, 4)
car.start()  # Inherited from Vehicle
car.honk()   # Specific to Car

print()

moto = Motorcycle("Harley", "Street 750", 2023, False)
moto.start()    # Inherited from Vehicle
moto.wheelie()  # Specific to Motorcycle


# ============================================================================
# EXAMPLE 3: Method Overriding
# ============================================================================

print("\n### Example 3: Method Overriding ###\n")

class Employee:
    """Parent class"""

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def calculate_bonus(self):
        """Base bonus calculation"""
        return self.salary * 0.05  # 5% bonus

    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Bonus: ${self.calculate_bonus():,.2f}")

class Manager(Employee):
    """Child class with overridden method"""

    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def calculate_bonus(self):
        """Managers get higher bonus"""
        return self.salary * 0.15  # 15% bonus

    def display_info(self):
        """Override and extend parent method"""
        super().display_info()  # Call parent version
        print(f"Department: {self.department}")  # Add extra info
        print(f"Role: Manager")

class Developer(Employee):
    """Another child class"""

    def __init__(self, name, employee_id, salary, programming_languages):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages

    def calculate_bonus(self):
        """Developers get bonus based on skills"""
        skill_bonus = len(self.programming_languages) * 0.02
        return self.salary * (0.10 + skill_bonus)

    def display_info(self):
        super().display_info()
        print(f"Languages: {', '.join(self.programming_languages)}")
        print(f"Role: Developer")

# Create employees
emp = Employee("Alice", "E001", 50000)
mgr = Manager("Bob", "M001", 80000, "Engineering")
dev = Developer("Charlie", "D001", 70000, ["Python", "Java", "JavaScript"])

print("Regular Employee:")
emp.display_info()

print("\nManager:")
mgr.display_info()

print("\nDeveloper:")
dev.display_info()


# ============================================================================
# EXAMPLE 4: Multi-Level Inheritance
# ============================================================================

print("\n### Example 4: Multi-Level Inheritance ###\n")

class LivingBeing:
    """Top-level parent"""

    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing")

class Mammal(LivingBeing):
    """Inherits from LivingBeing"""

    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def nurse_young(self):
        print(f"{self.name} nurses its young")

class Dog(Mammal):
    """Inherits from Mammal"""

    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} barks!")

# Dog has access to all parent methods
dog = Dog("Max", "Brown", "Labrador")
dog.breathe()      # From LivingBeing
dog.nurse_young()  # From Mammal
dog.bark()         # From Dog
print(f"Fur color: {dog.fur_color}")


# ============================================================================
# EXAMPLE 5: Multiple Inheritance
# ============================================================================

print("\n### Example 5: Multiple Inheritance ###\n")

class Flyer:
    """First parent class"""

    def fly(self):
        print(f"{self.name} is flying!")

class Swimmer:
    """Second parent class"""

    def swim(self):
        print(f"{self.name} is swimming!")

class Duck(Flyer, Swimmer):
    """Inherits from both Flyer and Swimmer"""

    def __init__(self, name):
        self.name = name

    def quack(self):
        print(f"{self.name} says: Quack!")

# Duck has methods from both parents
duck = Duck("Donald")
duck.fly()    # From Flyer
duck.swim()   # From Swimmer
duck.quack()  # From Duck


# ============================================================================
# EXAMPLE 6: Real-World Example - Banking System
# ============================================================================

print("\n### Example 6: Banking System Inheritance ###\n")

class BankAccount:
    """Base account class"""

    account_count = 0

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        BankAccount.account_count += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")

    def display_info(self):
        print(f"\nAccount: {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance:.2f}")

class SavingsAccount(BankAccount):
    """Savings account with interest"""

    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """Add monthly interest"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f}")

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.interest_rate*100}%")
        print(f"Type: Savings Account")

class CheckingAccount(BankAccount):
    """Checking account with overdraft"""

    def __init__(self, account_number, owner, balance=0, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Override to allow overdraft"""
        max_withdrawal = self.balance + self.overdraft_limit
        if amount > max_withdrawal:
            print(f"Exceeds overdraft limit!")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")
            if self.balance < 0:
                print(f"⚠️  Overdraft: ${abs(self.balance):.2f}")

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")
        print(f"Type: Checking Account")

# Create accounts
savings = SavingsAccount("SAV001", "Alice", 1000, 0.03)
checking = CheckingAccount("CHK001", "Bob", 500, 1000)

print("=== Savings Account ===")
savings.display_info()
savings.add_interest()
savings.deposit(500)

print("\n=== Checking Account ===")
checking.display_info()
checking.withdraw(700)  # Uses overdraft
checking.deposit(300)


# ============================================================================
# EXAMPLE 7: isinstance() and issubclass()
# ============================================================================

print("\n### Example 7: Type Checking ###\n")

# isinstance() - check if object is instance of class
print(f"savings is SavingsAccount: {isinstance(savings, SavingsAccount)}")
print(f"savings is BankAccount: {isinstance(savings, BankAccount)}")  # True (parent)
print(f"savings is CheckingAccount: {isinstance(savings, CheckingAccount)}")

# issubclass() - check if class is subclass of another
print(f"\nSavingsAccount is subclass of BankAccount: {issubclass(SavingsAccount, BankAccount)}")
print(f"CheckingAccount is subclass of BankAccount: {issubclass(CheckingAccount, BankAccount)}")
print(f"BankAccount is subclass of SavingsAccount: {issubclass(BankAccount, SavingsAccount)}")


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "="*70)
print("KEY TAKEAWAYS:")
print("="*70)
print("""
INHERITANCE = Creating new classes based on existing ones

SYNTAX:
    class ChildClass(ParentClass):
        pass

BENEFITS:
1. Code Reuse - don't repeat yourself
2. Extensibility - add new features to existing code
3. Hierarchy - model real-world relationships

SUPER():
- Call parent class methods
- Especially important in __init__
- super().__init__() calls parent constructor

METHOD OVERRIDING:
- Child can replace parent's method implementation
- Use same method name in child class
- Can still call parent method with super()

TYPES:
1. Single Inheritance - one parent
2. Multi-level Inheritance - grandparent → parent → child
3. Multiple Inheritance - multiple parents (use carefully!)

isinstance(obj, Class) - check if obj is instance of Class
issubclass(Child, Parent) - check if Child inherits from Parent

WHEN TO USE:
- "IS-A" relationship (Dog IS-A Animal)
- NOT for "HAS-A" relationship (Car HAS-A Engine - use composition)

BEST PRACTICES:
- Keep inheritance hierarchies shallow (2-3 levels)
- Use composition over inheritance when possible
- Don't inherit just for code reuse
- Ensure "is-a" relationship makes sense
""")

print("\nLesson 4 Complete! ✓")
print("Next: Run lessons/05_polymorphism.py")
