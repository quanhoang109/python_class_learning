# Python OOP Quick Start Guide

Get started with Object-Oriented Programming in Python in 30 minutes!

---

## What is OOP?

OOP = Programming with "objects" that contain data (attributes) and functions (methods).

**Think of it like:**
- **Class** = Cookie cutter (blueprint)
- **Object** = Cookie (instance made from blueprint)

---

## The 5-Minute Crash Course

### 1. Creating a Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def bark(self):  # method
        print(f"{self.name} says Woof!")
```

### 2. Creating Objects

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()  # Buddy says Woof!
print(dog2.age)  # 5
```

### 3. The Four Pillars

**Encapsulation** = Hide data, provide controlled access
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

**Inheritance** = Create new classes from existing ones
```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof!")

dog = Dog()
dog.eat()   # inherited method
dog.bark()  # own method
```

**Polymorphism** = Same interface, different implementations
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.speak())  # calls different speak() each time
```

**Abstraction** = Hide complex details
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
```

---

## Quick Reference

### Class Basics

```python
class MyClass:
    # Class attribute (shared by all instances)
    class_var = "shared"

    def __init__(self, value):
        # Instance attribute (unique to each instance)
        self.instance_var = value

    # Instance method
    def instance_method(self):
        return self.instance_var

    # Class method
    @classmethod
    def class_method(cls):
        return cls.class_var

    # Static method
    @staticmethod
    def static_method(x, y):
        return x + y
```

### Inheritance

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # call parent constructor
        self.age = age

    def greet(self):  # override parent method
        super().greet()  # optionally call parent method
        print(f"I'm {self.age} years old")
```

### Properties

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value

person = Person("Alice")
print(person.name)  # getter
person.name = "Bob"  # setter
```

### Magic Methods

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

book = Book("Python 101", 300)
print(book)  # calls __str__
print(len(book))  # calls __len__
```

---

## Common Patterns

### Singleton Pattern

```python
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory Pattern

```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
```

---

## Best Practices

### DO:
- ✅ Use meaningful class names (PascalCase)
- ✅ Keep classes focused (Single Responsibility)
- ✅ Use encapsulation for data protection
- ✅ Prefer composition over inheritance
- ✅ Write docstrings

```python
class BankAccount:
    """Represents a bank account with deposit and withdrawal capabilities."""

    def __init__(self, account_number, balance=0):
        """
        Initialize a bank account.

        Args:
            account_number (str): Unique account identifier
            balance (float): Initial balance (default 0)
        """
        self.account_number = account_number
        self.__balance = balance
```

### DON'T:
- ❌ Make everything a class (use functions when appropriate)
- ❌ Create deep inheritance hierarchies (max 2-3 levels)
- ❌ Use inheritance just for code reuse
- ❌ Expose all attributes publicly
- ❌ Forget to call super().__init__()

---

## Practice Exercises

### Exercise 1: Simple Class (5 min)

Create a `Car` class with make, model, year attributes and a `start()` method.

<details>
<summary>Solution</summary>

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"{self.year} {self.make} {self.model} is starting...")

car = Car("Toyota", "Camry", 2023)
car.start()
```
</details>

### Exercise 2: Encapsulation (10 min)

Create a `BankAccount` class with private balance and deposit/withdraw methods.

<details>
<summary>Solution</summary>

```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")
```
</details>

### Exercise 3: Inheritance (15 min)

Create `Animal`, `Dog`, and `Cat` classes with inheritance.

<details>
<summary>Solution</summary>

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

dog.make_sound()  # Woof!
cat.make_sound()  # Meow!
dog.sleep()       # inherited method
```
</details>

---

## Next Steps

1. **Run the lessons** in order:
   ```bash
   python lessons/01_classes_and_objects.py
   python lessons/02_attributes_and_methods.py
   python lessons/03_encapsulation.py
   python lessons/04_inheritance.py
   ```

2. **Complete exercises** in EXERCISES.md

3. **Build projects** in projects/ folder

4. **Learn design patterns** in the design-patterns-ecommerce/ folder

---

## Common Questions

**Q: When should I use OOP?**
A: When modeling real-world entities, building large applications, or when you need code reusability and organization.

**Q: What's the difference between a class and an object?**
A: Class is the blueprint, object is the instance. Like: Recipe (class) vs Actual Cake (object).

**Q: When to use inheritance vs composition?**
A: Use inheritance for "is-a" relationships (Dog IS-A Animal). Use composition for "has-a" relationships (Car HAS-A Engine).

**Q: What is `self`?**
A: `self` refers to the current instance of the class. It's how you access the object's own attributes and methods.

**Q: Why use private attributes?**
A: To protect data from invalid modifications and hide implementation details.

---

## Cheat Sheet

```python
# Class definition
class ClassName:
    class_var = "shared"  # class attribute

    def __init__(self, param):  # constructor
        self.param = param  # instance attribute

    def method(self):  # instance method
        return self.param

    @classmethod  # class method
    def cls_method(cls):
        return cls.class_var

    @staticmethod  # static method
    def static_method(x):
        return x * 2

    @property  # property
    def prop(self):
        return self._prop

# Inheritance
class Child(Parent):
    def __init__(self):
        super().__init__()  # call parent constructor

# Multiple inheritance
class Child(Parent1, Parent2):
    pass

# Check type
isinstance(obj, ClassName)
issubclass(ChildClass, ParentClass)
```

---

**Ready to dive deeper?** Start with `lessons/01_classes_and_objects.py`!
