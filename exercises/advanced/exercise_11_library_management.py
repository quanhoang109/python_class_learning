"""
Exercise 11: Library Management System

Create a complete library system with:

Classes:
- Book - title, author, isbn, is_available
- Member - name, member_id, borrowed_books (list)
- Library - books (list), members (list)

Features:
- Add/remove books and members
- Borrow book (check availability, update member's list)
- Return book
- Search books by title/author
- Display member's borrowed books
- Calculate late fees (if book held > 14 days)
"""

from datetime import datetime, timedelta

# TODO: Write your Book, Member, and Library classes here
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_date = None
        pass
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        pass
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        pass
    def add_book(self, book):
        self.books.append(book)
        pass
    def add_member(self, member):
        self.members.append(member)
        pass    
    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn and b.is_available), None)
        if member and book:
            book.is_available = False
            member.borrowed_books.append((book, datetime.now()))
        pass
    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member:
            for i, (book, borrow_date) in enumerate(member.borrowed_books):
                if book.isbn == isbn:
                    book.is_available = True
                    member.borrowed_books.pop(i)
                    break
        pass
    def search_books(self, query):
        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        return results
    def display_member_books(self, member_id): 
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member:
            for book, borrow_date in member.borrowed_books:
                print(f"{book.title} by {book.author}, borrowed on {borrow_date.strftime('%Y-%m-%d')}")
        pass
    def calculate_late_fees(self, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        total_fees = 0
        if member:
            for book, borrow_date in member.borrowed_books:
                days_borrowed = (datetime.now() - borrow_date).days
                if days_borrowed > 14:
                    total_fees += (days_borrowed - 14) * 0.50  # Assuming $0.50 per day late fee
        return total_fees
# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - TESTS")
    print("=" * 60)

    # ---------------------------------------------------------------------
    # Test 1: Basic Setup
    # ---------------------------------------------------------------------
    print("\n--- Test 1: Basic Setup ---")
    library = Library("City Library")

    book1 = Book("Python Programming", "John Doe", "ISBN-001")
    book2 = Book("Data Science Handbook", "Jane Smith", "ISBN-002")
    book3 = Book("Python for Beginners", "Bob Wilson", "ISBN-003")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")

    library.add_member(member1)
    library.add_member(member2)

    print(f"Library: {library.name}")
    print(f"Books added: {len(library.books)}")
    print(f"Members added: {len(library.members)}")
    assert len(library.books) == 3, "Should have 3 books"
    assert len(library.members) == 2, "Should have 2 members"
    print("✓ Basic setup passed!")

    # ---------------------------------------------------------------------
    # Test 2: Borrow and Return Books
    # ---------------------------------------------------------------------
    print("\n--- Test 2: Borrow and Return Books ---")

    library.borrow_book("M001", "ISBN-001")
    print(f"Alice borrowed: Python Programming")
    assert book1.is_available == False, "Book should be unavailable"
    assert len(member1.borrowed_books) == 1, "Alice should have 1 book"

    library.borrow_book("M002", "ISBN-002")
    print(f"Bob borrowed: Data Science Handbook")
    assert book2.is_available == False, "Book should be unavailable"

    # Try to borrow unavailable book
    library.borrow_book("M002", "ISBN-001")  # Already borrowed by Alice
    assert len(member2.borrowed_books) == 1, "Bob should still have only 1 book"
    print("✓ Cannot borrow unavailable book!")

    # Return book
    library.return_book("M001", "ISBN-001")
    print(f"Alice returned: Python Programming")
    assert book1.is_available == True, "Book should be available"
    assert len(member1.borrowed_books) == 0, "Alice should have 0 books"
    print("✓ Borrow and return passed!")

    # ---------------------------------------------------------------------
    # Test 3: Search Books
    # ---------------------------------------------------------------------
    print("\n--- Test 3: Search Books ---")

    results = library.search_books("Python")
    print(f"Search 'Python': Found {len(results)} books")
    assert len(results) == 2, "Should find 2 Python books"

    results = library.search_books("Jane")
    print(f"Search 'Jane': Found {len(results)} books")
    assert len(results) == 1, "Should find 1 book by Jane"

    results = library.search_books("xyz")
    print(f"Search 'xyz': Found {len(results)} books")
    assert len(results) == 0, "Should find no books"
    print("✓ Search passed!")

    # ---------------------------------------------------------------------
    # Test 4: Display Member Books
    # ---------------------------------------------------------------------
    print("\n--- Test 4: Display Member Books ---")
    library.borrow_book("M001", "ISBN-001")
    library.borrow_book("M001", "ISBN-003")
    print("Alice's borrowed books:")
    library.display_member_books("M001")
    print("✓ Display passed!")

    # ---------------------------------------------------------------------
    # Test 5: Late Fees - No Late Books
    # ---------------------------------------------------------------------
    print("\n--- Test 5: Late Fees - No Late Books ---")

    # Books just borrowed (today) - no late fees
    fees = library.calculate_late_fees("M001")
    print(f"Late fees for Alice (books borrowed today): ${fees:.2f}")
    assert fees == 0, "No late fees for books borrowed today"
    print("✓ No late fees for recent borrows!")

    # ---------------------------------------------------------------------
    # Test 6: Late Fees - Simulate Overdue Books
    # ---------------------------------------------------------------------
    print("\n--- Test 6: Late Fees - Overdue Books ---")

    # Create a new library for clean late fee testing
    late_library = Library("Test Library")
    late_book = Book("Overdue Book", "Test Author", "ISBN-LATE")
    late_library.add_book(late_book)

    late_member = Member("Charlie", "M003")
    late_library.add_member(late_member)

    # Manually add a book with a past borrow date (20 days ago)
    days_overdue = 20
    past_date = datetime.now() - timedelta(days=days_overdue)
    late_book.is_available = False
    late_member.borrowed_books.append((late_book, past_date))

    fees = late_library.calculate_late_fees("M003")
    expected_fees = (days_overdue - 14) * 0.50  # 6 days late * $0.50
    print(f"Book borrowed {days_overdue} days ago")
    print(f"Days overdue: {days_overdue - 14}")
    print(f"Late fees: ${fees:.2f}")
    print(f"Expected: ${expected_fees:.2f}")
    assert fees == expected_fees, f"Expected ${expected_fees:.2f} in late fees"
    print("✓ Late fees calculated correctly!")

    # ---------------------------------------------------------------------
    # Test 7: Late Fees - Multiple Overdue Books
    # ---------------------------------------------------------------------
    print("\n--- Test 7: Late Fees - Multiple Overdue Books ---")

    late_library2 = Library("Test Library 2")

    book_a = Book("Book A", "Author A", "ISBN-A")
    book_b = Book("Book B", "Author B", "ISBN-B")
    book_c = Book("Book C", "Author C", "ISBN-C")

    late_library2.add_book(book_a)
    late_library2.add_book(book_b)
    late_library2.add_book(book_c)

    heavy_borrower = Member("Diana", "M004")
    late_library2.add_member(heavy_borrower)

    # Add books with different overdue periods
    # Book A: 21 days ago (7 days late) = $3.50
    book_a.is_available = False
    heavy_borrower.borrowed_books.append((book_a, datetime.now() - timedelta(days=21)))

    # Book B: 30 days ago (16 days late) = $8.00
    book_b.is_available = False
    heavy_borrower.borrowed_books.append((book_b, datetime.now() - timedelta(days=30)))

    # Book C: 10 days ago (not late) = $0.00
    book_c.is_available = False
    heavy_borrower.borrowed_books.append((book_c, datetime.now() - timedelta(days=10)))

    fees = late_library2.calculate_late_fees("M004")
    expected_total = (7 * 0.50) + (16 * 0.50) + 0  # $3.50 + $8.00 + $0 = $11.50

    print(f"Book A: 21 days (7 days late) = $3.50")
    print(f"Book B: 30 days (16 days late) = $8.00")
    print(f"Book C: 10 days (not late) = $0.00")
    print(f"Total late fees: ${fees:.2f}")
    print(f"Expected: ${expected_total:.2f}")
    assert fees == expected_total, f"Expected ${expected_total:.2f} in total late fees"
    print("✓ Multiple late fees calculated correctly!")

    # ---------------------------------------------------------------------
    # Test 8: Late Fees - Edge Case (Exactly 14 days)
    # ---------------------------------------------------------------------
    print("\n--- Test 8: Late Fees - Edge Case (Exactly 14 days) ---")

    edge_library = Library("Edge Case Library")
    edge_book = Book("Edge Book", "Edge Author", "ISBN-EDGE")
    edge_library.add_book(edge_book)

    edge_member = Member("Eve", "M005")
    edge_library.add_member(edge_member)

    # Exactly 14 days - should NOT be late
    edge_book.is_available = False
    edge_member.borrowed_books.append((edge_book, datetime.now() - timedelta(days=14)))

    fees = edge_library.calculate_late_fees("M005")
    print(f"Book borrowed exactly 14 days ago")
    print(f"Late fees: ${fees:.2f}")
    assert fees == 0, "No late fees for exactly 14 days"
    print("✓ Edge case (14 days) passed - no fees!")

    # ---------------------------------------------------------------------
    # Test 9: Late Fees - 15 days (First day late)
    # ---------------------------------------------------------------------
    print("\n--- Test 9: Late Fees - First Day Late (15 days) ---")

    first_late_library = Library("First Late Library")
    first_late_book = Book("First Late Book", "Author", "ISBN-FIRST")
    first_late_library.add_book(first_late_book)

    first_late_member = Member("Frank", "M006")
    first_late_library.add_member(first_late_member)

    # 15 days - first day late
    first_late_book.is_available = False
    first_late_member.borrowed_books.append((first_late_book, datetime.now() - timedelta(days=15)))

    fees = first_late_library.calculate_late_fees("M006")
    print(f"Book borrowed 15 days ago (1 day late)")
    print(f"Late fees: ${fees:.2f}")
    assert fees == 0.50, "Should be $0.50 for 1 day late"
    print("✓ First day late fee correct!")

    # ---------------------------------------------------------------------
    # Test 10: Non-existent Member
    # ---------------------------------------------------------------------
    print("\n--- Test 10: Non-existent Member ---")

    fees = library.calculate_late_fees("INVALID")
    print(f"Late fees for non-existent member: ${fees:.2f}")
    assert fees == 0, "Should return 0 for non-existent member"
    print("✓ Non-existent member handled!")

    # ---------------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
