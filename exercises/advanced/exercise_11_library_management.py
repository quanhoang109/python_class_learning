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


# Test code (uncomment when ready)
# library = Library("City Library")
#
# book1 = Book("Python Programming", "John Doe", "ISBN-001")
# library.add_book(book1)
#
# member = Member("Alice", "M001")
# library.add_member(member)
#
# library.borrow_book("M001", "ISBN-001")
# library.display_member_books("M001")
# library.return_book("M001", "ISBN-001")
