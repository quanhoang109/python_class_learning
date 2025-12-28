# Exercise Solutions

This directory contains complete solutions to all exercises in the Python OOP Tutorial.

## How to Use Solutions

1. **Try First**: Attempt exercises on your own before looking at solutions
2. **Compare**: After solving, compare your solution with the provided one
3. **Learn**: Understand different approaches and best practices
4. **Experiment**: Modify solutions to deepen your understanding

## Solution Files

- **all_exercises.py**: Complete solutions for all exercises from EXERCISES.md
  - Beginner exercises (1-5)
  - Intermediate exercises (6-10)
  - Advanced exercises (11-15)
  - Challenge exercises

## Running Solutions

### Run All Demos
```bash
python solutions/all_exercises.py
```

### Import and Test Individual Solutions
```python
from solutions.all_exercises import Book, Student, BankAccount

# Test Book class
book = Book("Python OOP", "John Doe", 300, 29.99)
book.display_info()

# Test Student class
student = Student("Alice", "S001")
student.add_grade(95)
student.display_report_card()
```

### Demo Functions
The solutions file includes demo functions for each section:

```python
from solutions.all_exercises import (
    demo_beginner_exercises,
    demo_intermediate_exercises,
    demo_advanced_exercises
)

# Run specific demos
demo_beginner_exercises()
demo_intermediate_exercises()
demo_advanced_exercises()
```

## Solutions Organization

### Beginner Exercises (Lines 1-250)
1. **Book Class**: Basic class with methods
2. **Rectangle Class**: Geometric calculations
3. **Student Class**: Grade management
4. **Counter Class**: Class attributes and methods
5. **Temperature Class**: Class methods and static methods

### Intermediate Exercises (Lines 251-500)
6. **Bank Account**: Encapsulation with private attributes
7. **Animal Inheritance**: Method overriding
8. **Shape Hierarchy**: Abstract base classes
9. **Employee System**: Polymorphic salary calculation
10. **Shopping Cart**: Composition and aggregation

### Advanced Exercises (Lines 501-800)
11. **Library Management**: Complete system with multiple classes
12. **Game Characters**: RPG system with inventory
13. **Vehicle Rental**: Complex inheritance hierarchy
14. **Social Media**: Associations and relationships
15. **Hotel Reservation**: Date handling and validation

### Challenge Exercises (Lines 801+)
1. **Design Your Own**: Custom project examples
2. **Refactor Code**: Procedural to OOP transformation
3. **Multiple Inheritance**: MRO and diamond problem

## Coding Standards in Solutions

All solutions follow these standards:

### 1. Naming Conventions
- Classes: `PascalCase` (e.g., `ShoppingCart`)
- Methods: `snake_case` (e.g., `calculate_total()`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_ITEMS`)
- Private: `_single_underscore` or `__double_underscore`

### 2. Docstrings
Every class and method includes a docstring:
```python
class BankAccount:
    """Represents a bank account with encapsulated data."""

    def deposit(self, amount):
        """Deposit money into account."""
        # Implementation
```

### 3. Type Hints (where applicable)
```python
def calculate_total(self) -> float:
    """Calculate total cost."""
    return sum(item.price for item in self.items)
```

### 4. Error Handling
```python
def withdraw(self, amount):
    """Withdraw money."""
    if amount > self.balance:
        print("Insufficient funds")
        return False
    # Process withdrawal
```

## Best Practices Demonstrated

### Encapsulation
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    @property
    def balance(self):
        return self.__balance  # Read-only access
```

### Inheritance
```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"  # Override parent method
```

### Polymorphism
```python
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.make_sound()  # Same interface, different behavior
```

### Abstraction
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Subclasses must implement
```

## Common Patterns

### 1. Builder Pattern (in complex classes)
```python
class CharacterBuilder:
    def with_name(self, name):
        self.name = name
        return self

    def with_health(self, health):
        self.health = health
        return self

    def build(self):
        return Character(self.name, self.health)
```

### 2. Factory Pattern (creating objects)
```python
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == 'circle':
            return Circle(*args)
        elif shape_type == 'rectangle':
            return Rectangle(*args)
```

### 3. Singleton Pattern (one instance)
```python
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

## Testing Your Understanding

After reviewing solutions, try these:

1. **Modify**: Change the solution to add new features
2. **Extend**: Add inheritance or new methods
3. **Combine**: Mix solutions to create something new
4. **Optimize**: Improve performance or readability
5. **Test**: Write unit tests for the solutions

## Getting Help

If you don't understand a solution:

1. Read the comments in the code
2. Check the corresponding lesson file
3. Run the demo function to see it in action
4. Experiment with the code in a Python REPL
5. Refer back to lessons for concept explanations

## Next Steps

After mastering these solutions:

1. Complete the projects in `projects/` directory
2. Create your own custom classes
3. Build a complete application using OOP
4. Study design patterns
5. Explore advanced topics (metaclasses, descriptors)

## Contributing

Found a better solution or spotted an issue?
- Solutions can always be improved
- Different approaches are valid
- Learning is about understanding, not memorization

Happy coding! 🚀
