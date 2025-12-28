# Python OOP Exercises

Hands-on exercises to practice Object-Oriented Programming concepts.

---

## Beginner Exercises

### Exercise 1: Create a Book Class

Create a `Book` class with the following:
- Attributes: `title`, `author`, `pages`, `price`, `is_available`
- Methods:
  - `display_info()` - print book details
  - `apply_discount(percent)` - reduce price by percentage
  - `borrow()` - set is_available to False
  - `return_book()` - set is_available to True

**Test your class:**
```python
book = Book("Python Basics", "John Smith", 350, 29.99, True)
book.display_info()
book.apply_discount(10)
book.borrow()
book.display_info()
```

---

### Exercise 2: Rectangle Class

Create a `Rectangle` class with:
- Attributes: `width`, `height`
- Methods:
  - `area()` - return width * height
  - `perimeter()` - return 2 * (width + height)
  - `is_square()` - return True if width == height
  - `scale(factor)` - multiply both dimensions by factor

---

### Exercise 3: Student Class

Create a `Student` class with:
- Attributes: `name`, `student_id`, `grades` (list)
- Methods:
  - `add_grade(grade)` - add grade to list (0-100 validation)
  - `get_average()` - return average of all grades
  - `get_letter_grade()` - convert average to letter (A/B/C/D/F)
  - `display_report_card()` - show all info

---

### Exercise 4: Counter Class

Create a `Counter` class with:
- Class attribute: `total_counters`
- Instance attribute: `count` (starts at 0)
- Methods:
  - `increment()` - add 1 to count
  - `decrement()` - subtract 1 from count
  - `reset()` - set count to 0
  - `get_count()` - return current count
- Class method: `get_total_counters()`

---

### Exercise 5: Temperature Class

Create a `Temperature` class with:
- Instance attribute: `celsius`
- Instance methods:
  - `to_fahrenheit()` - return (celsius * 9/5) + 32
  - `to_kelvin()` - return celsius + 273.15
- Class method:
  - `from_fahrenheit(f)` - create Temperature from Fahrenheit
  - `from_kelvin(k)` - create Temperature from Kelvin
- Static method:
  - `is_freezing(celsius)` - return True if <= 0

---

## Intermediate Exercises

### Exercise 6: Bank Account with Encapsulation

Create a `BankAccount` class with:
- Private attributes: `__account_number`, `__balance`, `__owner`
- Public methods:
  - `deposit(amount)` - add money (validate > 0)
  - `withdraw(amount)` - remove money (check sufficient funds)
  - `get_balance()` - return balance
  - `transfer(amount, target_account)` - transfer to another account
- Properties:
  - `owner` - read-only property
  - `account_number` - read-only property

---

### Exercise 7: Animal Inheritance

Create an inheritance hierarchy:

**Base class `Animal`:**
- Attributes: `name`, `age`, `species`
- Methods: `eat()`, `sleep()`, `make_sound()` (prints generic sound)

**Child classes:**
- `Dog(Animal)` - override `make_sound()` to bark
- `Cat(Animal)` - override `make_sound()` to meow
- `Bird(Animal)` - add `fly()` method

Create a list of different animals and call `make_sound()` on each.

---

### Exercise 8: Shape Hierarchy

Create shape classes with inheritance:

**Base class `Shape`:**
- Abstract methods: `area()`, `perimeter()`

**Child classes:**
- `Circle(Shape)` - attributes: radius
- `Rectangle(Shape)` - attributes: width, height
- `Triangle(Shape)` - attributes: side1, side2, side3

Each should implement `area()` and `perimeter()`.

Create a function `total_area(shapes)` that calculates total area of a list of shapes.

---

### Exercise 9: Employee System

Create an employee management system:

**Base class `Employee`:**
- Attributes: `name`, `employee_id`, `base_salary`
- Methods: `calculate_salary()`, `display_info()`

**Child classes:**
- `FullTimeEmployee(Employee)` - gets full salary + benefits ($500)
- `PartTimeEmployee(Employee)` - `hours_worked` * `hourly_rate`
- `Contractor(Employee)` - `project_fee` (fixed amount)

Override `calculate_salary()` in each child class.

---

### Exercise 10: Shopping Cart

Create an e-commerce shopping cart:

**Class `Product`:**
- Attributes: `name`, `price`, `quantity_available`
- Methods: `reduce_stock(amount)`, `display()`

**Class `CartItem`:**
- Attributes: `product`, `quantity`
- Methods: `get_subtotal()`

**Class `ShoppingCart`:**
- Attributes: `items` (list of CartItems)
- Methods:
  - `add_item(product, quantity)` - check stock availability
  - `remove_item(product_name)`
  - `get_total()` - sum of all subtotals
  - `checkout()` - display items and total

---

## Advanced Exercises

### Exercise 11: Library Management System

Create a complete library system with:

**Classes:**
- `Book` - title, author, isbn, is_available
- `Member` - name, member_id, borrowed_books (list)
- `Library` - books (list), members (list)

**Features:**
- Add/remove books and members
- Borrow book (check availability, update member's list)
- Return book
- Search books by title/author
- Display member's borrowed books
- Calculate late fees (if book held > 14 days)

---

### Exercise 12: Game Character System

Create an RPG character system:

**Base class `Character`:**
- Attributes: name, health, attack_power, defense
- Methods: `take_damage(amount)`, `attack(target)`, `is_alive()`

**Child classes:**
- `Warrior` - high health, medium attack, special: `shield_block()`
- `Mage` - low health, high attack, special: `cast_spell(spell_name)`
- `Archer` - medium health, medium attack, special: `rapid_fire()`

**Class `Inventory`:**
- Store items, add/remove items, display items

Add inventory system to characters.

---

### Exercise 13: Vehicle Rental System

Create a vehicle rental system:

**Classes:**
- `Vehicle` (base) - brand, model, year, daily_rate, is_rented
- `Car(Vehicle)` - seats, fuel_type
- `Motorcycle(Vehicle)` - engine_size
- `Truck(Vehicle)` - cargo_capacity
- `Customer` - name, customer_id, rented_vehicles (list)
- `RentalAgency` - vehicles (list), customers (list)

**Features:**
- Add vehicles and customers
- Rent vehicle (check availability, add to customer)
- Return vehicle
- Calculate rental cost (days * daily_rate)
- Display available vehicles
- Get customer's rental history

---

### Exercise 14: Social Media System

Create a simple social media platform:

**Classes:**
- `User` - username, email, posts (list), friends (list)
- `Post` - content, author, timestamp, likes (list)
- `Comment` - content, author, timestamp
- `Platform` - users (list), all_posts (list)

**Features:**
- Create users
- Add/remove friends
- Create posts
- Like posts
- Add comments to posts
- Display user's feed (their posts + friends' posts)
- Search users

---

### Exercise 15: Hotel Reservation System

Create a hotel booking system:

**Classes:**
- `Room` - room_number, room_type, price_per_night, is_available
- `Reservation` - room, customer, check_in, check_out, total_cost
- `Customer` - name, email, reservations (list)
- `Hotel` - rooms (list), reservations (list)

**Features:**
- Add rooms
- Check availability for date range
- Make reservation (check conflicts)
- Cancel reservation
- Calculate total cost
- Display available rooms by type
- Get customer's reservation history

---

## Project Exercises

### Project 1: ATM Machine Simulator

Build a complete ATM system:
- Multiple account types (checking, savings)
- PIN authentication
- Deposit, withdraw, transfer
- Transaction history
- Multiple users
- Daily withdrawal limits

**Requirements:**
- Use encapsulation for sensitive data
- Use inheritance for account types
- Use proper error handling
- Save/load data (optional)

---

### Project 2: Restaurant Ordering System

Build a restaurant management system:
- Menu with items and prices
- Customer orders
- Kitchen queue
- Bill calculation with tax and tip
- Inventory management
- Daily sales report

**Classes needed:**
- MenuItem, Order, Customer, Kitchen, Restaurant

---

### Project 3: School Management System

Build a school administration system:
- Students, teachers, courses
- Enrollment system
- Grade management
- Attendance tracking
- Report cards
- Class schedules

**Features:**
- Add students/teachers
- Create courses
- Enroll students in courses
- Record grades and attendance
- Generate reports

---

## Challenge Exercises

### Challenge 1: Design Your Own

Pick a real-world system and design it using OOP:
- Fitness tracking app
- Task management system
- Movie rental service
- Online marketplace
- Hospital management
- Airline booking system

**Requirements:**
- At least 5 classes
- Use all 4 OOP pillars (Encapsulation, Inheritance, Polymorphism, Abstraction)
- Include properties and class methods
- Write comprehensive documentation

---

### Challenge 2: Refactor Procedural Code

Take this procedural code and refactor it using OOP:

```python
# Procedural approach
students = {}
grades = {}

def add_student(name, student_id):
    students[student_id] = name
    grades[student_id] = []

def add_grade(student_id, grade):
    if student_id in grades:
        grades[student_id].append(grade)

def get_average(student_id):
    if student_id in grades and grades[student_id]:
        return sum(grades[student_id]) / len(grades[student_id])
    return 0
```

Refactor into proper OOP with Student class, validation, properties, etc.

---

### Challenge 3: Multiple Inheritance

Create a class that uses multiple inheritance effectively:

Example: `FlyingFish` that inherits from both `Fish` and `Bird`

Show how to handle method resolution order (MRO) and avoid the diamond problem.

---

## Solutions

Solutions to all exercises are available in the `solutions/` folder.

**Tips:**
1. Try to solve without looking at solutions
2. Test your code thoroughly
3. Use type hints (optional but recommended)
4. Write docstrings for classes and methods
5. Handle edge cases and errors

---

## Progress Tracker

### Beginner
- [ ] Exercise 1: Book Class
- [ ] Exercise 2: Rectangle Class
- [ ] Exercise 3: Student Class
- [ ] Exercise 4: Counter Class
- [ ] Exercise 5: Temperature Class

### Intermediate
- [ ] Exercise 6: Bank Account
- [ ] Exercise 7: Animal Inheritance
- [ ] Exercise 8: Shape Hierarchy
- [ ] Exercise 9: Employee System
- [ ] Exercise 10: Shopping Cart

### Advanced
- [ ] Exercise 11: Library Management
- [ ] Exercise 12: Game Characters
- [ ] Exercise 13: Vehicle Rental
- [ ] Exercise 14: Social Media
- [ ] Exercise 15: Hotel Reservation

### Projects
- [ ] Project 1: ATM Machine
- [ ] Project 2: Restaurant System
- [ ] Project 3: School Management

### Challenges
- [ ] Challenge 1: Design Your Own
- [ ] Challenge 2: Refactor Code
- [ ] Challenge 3: Multiple Inheritance

**Good luck and happy coding!** 🚀
