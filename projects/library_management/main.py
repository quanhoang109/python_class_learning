"""
Library Management System - Complete Project
=============================================

A comprehensive library system demonstrating:
- Encapsulation (private data)
- Inheritance (different book/member types)
- Composition (Library has Books and Members)
- Association (Members borrow Books)

Run: python projects/library_management/main.py
"""

from datetime import datetime, timedelta
from typing import List, Optional


class Book:
    """Represents a book in the library."""

    def __init__(self, title: str, author: str, isbn: str, category: str = "General"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.is_available = True
        self.borrowed_date: Optional[datetime] = None
        self.borrowed_by: Optional['Member'] = None

    def borrow(self, member: 'Member') -> bool:
        """Mark book as borrowed."""
        if not self.is_available:
            return False

        self.is_available = False
        self.borrowed_date = datetime.now()
        self.borrowed_by = member
        return True

    def return_book(self) -> int:
        """Return book and calculate days borrowed."""
        if self.is_available:
            return 0

        days_borrowed = (datetime.now() - self.borrowed_date).days
        self.is_available = True
        self.borrowed_date = None
        self.borrowed_by = None
        return days_borrowed

    def calculate_late_fee(self, borrow_period: int = 14, fee_per_day: float = 0.50) -> float:
        """Calculate late fee if applicable."""
        if self.is_available or self.borrowed_date is None:
            return 0.0

        days_borrowed = (datetime.now() - self.borrowed_date).days
        days_late = max(0, days_borrowed - borrow_period)
        return days_late * fee_per_day

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by.name}"
        return f"'{self.title}' by {self.author} [{self.category}] - {status}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"


class DigitalBook(Book):
    """Represents a digital/ebook."""

    def __init__(self, title: str, author: str, isbn: str, file_format: str, file_size_mb: float):
        super().__init__(title, author, isbn, "Digital")
        self.file_format = file_format
        self.file_size_mb = file_size_mb
        self.download_count = 0

    def borrow(self, member: 'Member') -> bool:
        """Digital books are always available (unlimited copies)."""
        self.download_count += 1
        return True

    def return_book(self) -> int:
        """Digital books don't need to be returned."""
        return 0

    def calculate_late_fee(self, borrow_period: int = 14, fee_per_day: float = 0.50) -> float:
        """No late fees for digital books."""
        return 0.0

    def __str__(self):
        return f"[EBOOK] '{self.title}' by {self.author} ({self.file_format}, {self.file_size_mb}MB) - Downloads: {self.download_count}"


class Member:
    """Represents a library member."""

    member_id_counter = 1000

    def __init__(self, name: str, email: str, member_type: str = "Regular"):
        self.member_id = f"M{Member.member_id_counter:04d}"
        Member.member_id_counter += 1
        self.name = name
        self.email = email
        self.member_type = member_type  # Regular, Premium, Student
        self.borrowed_books: List[Book] = []
        self.total_books_borrowed = 0
        self.total_late_fees = 0.0

    @property
    def max_books(self) -> int:
        """Maximum books allowed based on member type."""
        limits = {
            "Regular": 3,
            "Premium": 10,
            "Student": 5
        }
        return limits.get(self.member_type, 3)

    @property
    def borrow_period_days(self) -> int:
        """Borrow period based on member type."""
        periods = {
            "Regular": 14,
            "Premium": 30,
            "Student": 21
        }
        return periods.get(self.member_type, 14)

    def can_borrow_more(self) -> bool:
        """Check if member can borrow more books."""
        return len(self.borrowed_books) < self.max_books

    def borrow_book(self, book: Book) -> bool:
        """Borrow a book."""
        if not self.can_borrow_more():
            print(f"Error: {self.name} has reached maximum borrow limit ({self.max_books} books)")
            return False

        if book.borrow(self):
            self.borrowed_books.append(book)
            self.total_books_borrowed += 1
            return True

        return False

    def return_book(self, book: Book) -> float:
        """Return a book and pay late fee if applicable."""
        if book not in self.borrowed_books:
            print(f"Error: {self.name} hasn't borrowed this book")
            return 0.0

        late_fee = book.calculate_late_fee(self.borrow_period_days)
        days_borrowed = book.return_book()

        self.borrowed_books.remove(book)
        self.total_late_fees += late_fee

        return late_fee

    def __str__(self):
        return f"{self.name} ({self.member_id}) - {self.member_type} | Books: {len(self.borrowed_books)}/{self.max_books}"


class Library:
    """Represents the library management system."""

    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.members: List[Member] = []
        self.total_borrows = 0

    def add_book(self, book: Book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"✓ Added book: {book.title}")

    def add_member(self, member: Member):
        """Add a member to the library."""
        self.members.append(member)
        print(f"✓ Registered member: {member.name} ({member.member_id})")

    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """Find a book by ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member_by_id(self, member_id: str) -> Optional[Member]:
        """Find a member by ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def search_books(self, query: str) -> List[Book]:
        """Search books by title or author."""
        query = query.lower()
        results = []
        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)
        return results

    def borrow_book(self, member_id: str, isbn: str) -> bool:
        """Process a book borrow request."""
        member = self.find_member_by_id(member_id)
        if not member:
            print(f"Error: Member {member_id} not found")
            return False

        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"Error: Book with ISBN {isbn} not found")
            return False

        if not book.is_available and not isinstance(book, DigitalBook):
            print(f"Error: '{book.title}' is currently borrowed")
            return False

        if member.borrow_book(book):
            self.total_borrows += 1
            print(f"✓ {member.name} borrowed '{book.title}'")
            return True

        return False

    def return_book(self, member_id: str, isbn: str) -> bool:
        """Process a book return."""
        member = self.find_member_by_id(member_id)
        if not member:
            print(f"Error: Member {member_id} not found")
            return False

        book = self.find_book_by_isbn(isbn)
        if not book:
            print(f"Error: Book with ISBN {isbn} not found")
            return False

        late_fee = member.return_book(book)
        if late_fee > 0:
            print(f"✓ {member.name} returned '{book.title}' - Late fee: ${late_fee:.2f}")
        else:
            print(f"✓ {member.name} returned '{book.title}'")

        return True

    def display_available_books(self):
        """Display all available books."""
        print(f"\n{'='*70}")
        print(f"{self.name} - Available Books")
        print(f"{'='*70}")

        available = [book for book in self.books if book.is_available or isinstance(book, DigitalBook)]

        if not available:
            print("No books currently available")
        else:
            for book in available:
                print(f"  {book}")

        print(f"{'='*70}\n")

    def display_member_books(self, member_id: str):
        """Display books borrowed by a member."""
        member = self.find_member_by_id(member_id)
        if not member:
            print(f"Error: Member {member_id} not found")
            return

        print(f"\n{'='*70}")
        print(f"Books Borrowed by {member.name} ({member.member_id})")
        print(f"{'='*70}")

        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book in member.borrowed_books:
                late_fee = book.calculate_late_fee(member.borrow_period_days)
                late_info = f" - Late fee: ${late_fee:.2f}" if late_fee > 0 else ""
                print(f"  {book.title} by {book.author}{late_info}")

        print(f"{'='*70}\n")

    def display_statistics(self):
        """Display library statistics."""
        print(f"\n{'='*70}")
        print(f"{self.name} - Statistics")
        print(f"{'='*70}")

        total_books = len(self.books)
        available_books = sum(1 for book in self.books if book.is_available)
        borrowed_books = total_books - available_books

        print(f"Total Books: {total_books}")
        print(f"  Available: {available_books}")
        print(f"  Borrowed: {borrowed_books}")
        print(f"\nTotal Members: {len(self.members)}")
        print(f"Total Borrows (all time): {self.total_borrows}")

        total_fees = sum(member.total_late_fees for member in self.members)
        print(f"Total Late Fees Collected: ${total_fees:.2f}")

        print(f"{'='*70}\n")

    def display_all_members(self):
        """Display all library members."""
        print(f"\n{'='*70}")
        print(f"{self.name} - All Members")
        print(f"{'='*70}")

        for member in self.members:
            print(f"  {member}")

        print(f"{'='*70}\n")


def demo_library_system():
    """Demonstrate the complete library management system."""
    print("="*70)
    print("LIBRARY MANAGEMENT SYSTEM DEMO")
    print("="*70)

    # Create library
    library = Library("City Central Library")

    # Add books
    print("\n--- Adding Books ---")
    library.add_book(Book("Python Programming", "John Doe", "ISBN-001", "Technology"))
    library.add_book(Book("Data Science Handbook", "Jane Smith", "ISBN-002", "Technology"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "ISBN-003", "Fiction"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "ISBN-004", "Fiction"))
    library.add_book(DigitalBook("Python for Beginners", "Alice Johnson", "ISBN-005", "PDF", 5.2))

    # Add members
    print("\n--- Registering Members ---")
    library.add_member(Member("Alice Williams", "alice@email.com", "Premium"))
    library.add_member(Member("Bob Johnson", "bob@email.com", "Regular"))
    library.add_member(Member("Charlie Brown", "charlie@email.com", "Student"))

    # Display initial state
    library.display_available_books()
    library.display_all_members()

    # Borrow books
    print("\n--- Borrowing Books ---")
    library.borrow_book("M1000", "ISBN-001")  # Alice borrows Python Programming
    library.borrow_book("M1001", "ISBN-002")  # Bob borrows Data Science
    library.borrow_book("M1002", "ISBN-003")  # Charlie borrows Gatsby
    library.borrow_book("M1000", "ISBN-005")  # Alice downloads ebook

    # Display member's books
    library.display_member_books("M1000")

    # Search books
    print("\n--- Searching Books ---")
    results = library.search_books("python")
    print(f"Search results for 'python':")
    for book in results:
        print(f"  {book}")

    # Return books
    print("\n--- Returning Books ---")
    library.return_book("M1001", "ISBN-002")  # Bob returns book

    # Display statistics
    library.display_statistics()

    # Try to borrow unavailable book
    print("\n--- Testing Error Handling ---")
    library.borrow_book("M1001", "ISBN-001")  # Try to borrow already borrowed book

    # Display final state
    library.display_available_books()


if __name__ == "__main__":
    demo_library_system()
