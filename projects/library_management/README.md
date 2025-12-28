# Library Management System Project

A complete library management system demonstrating advanced OOP concepts.

## Features

### Book Types
- **Physical Books**: Limited availability, can be borrowed by one person at a time
- **Digital Books (eBooks)**: Unlimited copies, always available, no late fees

### Member Types
- **Regular**: 3 books max, 14-day borrow period
- **Premium**: 10 books max, 30-day borrow period
- **Student**: 5 books max, 21-day borrow period

### Operations
- Add books and members
- Borrow and return books
- Search books by title/author
- Calculate late fees ($0.50/day after due date)
- View borrowing history
- Library statistics

## OOP Concepts Demonstrated

### 1. Encapsulation
- Private/protected data hiding
- Properties for max_books and borrow_period_days
- Controlled access to member data

### 2. Inheritance
```
Book
└── DigitalBook

Member (base class)
```

### 3. Composition
- Library **has** Books
- Library **has** Members
- Member **has** borrowed_books list

### 4. Association
- Members borrow Books (bidirectional relationship)
- Books track which Member borrowed them

## Class Relationships

```
┌──────────────┐         ┌─────────────┐
│   Library    │◆────────│    Book     │
│              │         │             │
│              │         │  - title    │
│ - books[]    │         │  - author   │
│ - members[]  │         │  - isbn     │
└──────┬───────┘         │  - borrowed_by
       │                 └──────△──────┘
       │◆                       │
       │                        │
       │                        │ inheritance
┌──────▼───────┐         ┌─────┴────────┐
│   Member     │◇────────│ DigitalBook  │
│              │borrows  │              │
│ - borrowed[] │         │ - file_format│
│ - member_id  │         │ - file_size  │
└──────────────┘         └──────────────┘
```

Legend:
- ◆ Composition (strong ownership)
- ◇ Aggregation (weak ownership)
- △ Inheritance

## Running the Project

```bash
python projects/library_management/main.py
```

## Usage Example

```python
# Create library
library = Library("City Library")

# Add books
library.add_book(Book("Python 101", "John Doe", "ISBN-001"))
library.add_book(DigitalBook("Learn OOP", "Jane Smith", "ISBN-002", "PDF", 5.5))

# Register members
library.add_member(Member("Alice", "alice@email.com", "Premium"))

# Borrow books
library.borrow_book("M1000", "ISBN-001")

# View member's books
library.display_member_books("M1000")

# Return and calculate late fee
library.return_book("M1000", "ISBN-001")

# Statistics
library.display_statistics()
```

## Late Fee Calculation

Late fees are calculated based on member type:
- **Regular**: 14 days free, then $0.50/day
- **Premium**: 30 days free, then $0.50/day
- **Student**: 21 days free, then $0.50/day
- **Digital Books**: No late fees

Example:
```python
# Regular member borrows for 20 days
# Late days = 20 - 14 = 6 days
# Fee = 6 * $0.50 = $3.00
```

## Extension Ideas

1. **Reservations**: Allow members to reserve borrowed books
2. **Notifications**: Email reminders for due dates
3. **Fines Management**: Payment tracking system
4. **Book Ratings**: Members can rate and review books
5. **Categories**: Browse books by category/genre
6. **Multi-Branch**: Support for multiple library branches
7. **Database Integration**: Persist data to database
8. **Web Interface**: Flask/Django web app
9. **Book Damage**: Track and charge for book condition
10. **Renewal System**: Allow members to extend borrow period

## Design Patterns Used

- **Factory Pattern**: Creating different member types
- **Observer Pattern**: Could be added for notifications
- **Strategy Pattern**: Different late fee calculations
- **Repository Pattern**: Library acts as book/member repository

## Testing

Run the demo to see all features in action:

```bash
python projects/library_management/main.py
```

Expected output:
- Book additions
- Member registrations
- Borrow transactions
- Return with late fees
- Search functionality
- Statistics reporting
