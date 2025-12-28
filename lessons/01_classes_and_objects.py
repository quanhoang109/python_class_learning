"""
LESSON 1: CLASSES AND OBJECTS
==============================

Learn the fundamentals of OOP in Python.

Key Concepts:
- What is a class?
- What is an object?
- How to create classes
- How to create objects
- The __init__ method
- The self keyword
"""

# ============================================================================
# WHAT IS A CLASS?
# ============================================================================
# A class is a blueprint or template for creating objects.
# Think of it like a cookie cutter - the cutter is the class,
# and each cookie you make is an object.

print("="*70)
print("LESSON 1: CLASSES AND OBJECTS")
print("="*70)

# ============================================================================
# EXAMPLE 1: Creating Your First Class
# ============================================================================

print("\n### Example 1: Simple Class ###\n")

class Dog:
    """A simple Dog class"""
    pass  # Empty class for now

# Create objects (instances) from the class
dog1 = Dog()
dog2 = Dog()

print(f"dog1 is a: {type(dog1)}")
print(f"dog2 is a: {type(dog2)}")
print(f"Are they the same object? {dog1 is dog2}")  # False - different objects
print(f"Are they the same type? {type(dog1) == type(dog2)}")  # True


# ============================================================================
# EXAMPLE 2: Adding Attributes to Objects
# ============================================================================

print("\n### Example 2: Adding Attributes ###\n")

# You can add attributes to objects after creation
dog1.name = "Buddy"
dog1.age = 3
dog1.breed = "Golden Retriever"

dog2.name = "Max"
dog2.age = 5
dog2.breed = "German Shepherd"

print(f"{dog1.name} is a {dog1.age} year old {dog1.breed}")
print(f"{dog2.name} is a {dog2.age} year old {dog2.breed}")


# ============================================================================
# EXAMPLE 3: Using __init__ (Constructor)
# ============================================================================

print("\n### Example 3: Constructor Method ###\n")

class Cat:
    """A Cat class with constructor"""

    def __init__(self, name, age, color):
        """
        Constructor - automatically called when creating object.

        Parameters:
        - self: reference to the current instance
        - name, age, color: parameters passed when creating object
        """
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute
        self.color = color  # Instance attribute
        print(f"A new cat named {name} was created!")

# Now we must provide arguments when creating objects
cat1 = Cat("Whiskers", 2, "Orange")
cat2 = Cat("Shadow", 4, "Black")

print(f"\n{cat1.name} is {cat1.age} years old and is {cat1.color}")
print(f"{cat2.name} is {cat2.age} years old and is {cat2.color}")


# ============================================================================
# EXAMPLE 4: Understanding 'self'
# ============================================================================

print("\n### Example 4: The 'self' Keyword ###\n")

class Person:
    """A Person class demonstrating 'self'"""

    def __init__(self, name, age):
        self.name = name  # 'self' refers to THIS specific object
        self.age = age

    def introduce(self):
        """Method to introduce the person"""
        # 'self' lets us access THIS object's attributes
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

    def have_birthday(self):
        """Increase age by 1"""
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age}")

# Create persons
alice = Person("Alice", 25)
bob = Person("Bob", 30)

# Call methods
alice.introduce()
bob.introduce()

# When we call alice.introduce(), 'self' inside the method refers to alice
# When we call bob.introduce(), 'self' inside the method refers to bob

alice.have_birthday()
alice.introduce()


# ============================================================================
# EXAMPLE 5: Real-World Example - Bank Account
# ============================================================================

print("\n### Example 5: Bank Account Class ###\n")

class BankAccount:
    """Represents a bank account"""

    def __init__(self, account_number, owner_name, balance=0):
        """
        Initialize bank account

        Parameters:
        - account_number: unique account identifier
        - owner_name: name of account owner
        - balance: initial balance (default 0)
        """
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Remove money from account"""
        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance:.2f}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive!")

    def get_balance(self):
        """Return current balance"""
        return self.balance

    def display_info(self):
        """Display account information"""
        print(f"\nAccount Number: {self.account_number}")
        print(f"Owner: {self.owner_name}")
        print(f"Balance: ${self.balance:.2f}")

# Create account
account = BankAccount("12345", "John Doe", 1000)

# Use the account
account.display_info()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Insufficient funds
account.display_info()


# ============================================================================
# EXAMPLE 6: Class with Multiple Methods
# ============================================================================

print("\n### Example 6: Student Class ###\n")

class Student:
    """Represents a student"""

    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.grades = []  # Empty list to store grades
        self.enrolled = True

    def add_grade(self, grade):
        """Add a grade to the student's record"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Grade {grade} added for {self.name}")
        else:
            print("Grade must be between 0 and 100!")

    def get_average(self):
        """Calculate average grade"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Convert average to letter grade"""
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display_report(self):
        """Display student report"""
        print(f"\n{'='*40}")
        print(f"Student Report")
        print(f"{'='*40}")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"Status: {'Enrolled' if self.enrolled else 'Graduated'}")
        print(f"{'='*40}\n")

# Create student
student = Student("Emma Wilson", "S12345", "Computer Science")

# Add some grades
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.add_grade(88)

# Display report
student.display_report()


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "="*70)
print("KEY TAKEAWAYS:")
print("="*70)
print("""
1. CLASS = Blueprint/Template for creating objects
   Example: class Dog:

2. OBJECT = Specific instance created from a class
   Example: my_dog = Dog()

3. __init__ = Constructor method, runs when object is created
   - First parameter is always 'self'
   - Used to initialize object attributes

4. self = Reference to the current object instance
   - Allows access to object's own attributes and methods
   - Must be first parameter in instance methods

5. ATTRIBUTES = Variables that belong to an object
   Example: self.name = "Buddy"

6. METHODS = Functions that belong to a class
   Example: def bark(self):

7. Creating Objects: object_name = ClassName(arguments)
   Example: dog = Dog("Buddy", 3)
""")


# ============================================================================
# PRACTICE EXERCISES
# ============================================================================

print("\n" + "="*70)
print("PRACTICE EXERCISES:")
print("="*70)
print("""
1. Create a 'Book' class with:
   - Attributes: title, author, pages, price
   - Method: display_info()

2. Create a 'Rectangle' class with:
   - Attributes: width, height
   - Methods: area(), perimeter(), is_square()

3. Create a 'Car' class with:
   - Attributes: make, model, year, mileage
   - Methods: drive(distance), display_info()

4. Create a 'ShoppingCart' class with:
   - Attributes: items (list), total
   - Methods: add_item(name, price), remove_item(name), get_total()

5. Create an 'Employee' class with:
   - Attributes: name, id, salary, department
   - Methods: give_raise(amount), change_department(new_dept), display_info()

Try to solve these on your own before looking at the solutions!
""")


if __name__ == "__main__":
    print("\nLesson 1 Complete! ✓")
    print("Next: Run lessons/02_attributes_and_methods.py")
