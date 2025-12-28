"""
Lesson 7: Magic Methods in Python
==================================

Magic methods (also called dunder methods - double underscore) allow you to
define how objects behave with built-in Python operations.

Key Concepts:
1. Object initialization and representation (__init__, __str__, __repr__)
2. Comparison operators (__eq__, __lt__, __le__, __gt__, __ge__, __ne__)
3. Arithmetic operators (__add__, __sub__, __mul__, __truediv__)
4. Container methods (__len__, __getitem__, __setitem__, __contains__)
5. Callable objects (__call__)
6. Context managers (__enter__, __exit__)

Run this file: python lessons/07_magic_methods.py
"""


# =============================================================================
# 1. INITIALIZATION AND REPRESENTATION
# =============================================================================

class Book:
    """Book class demonstrating __init__, __str__, and __repr__."""

    def __init__(self, title, author, pages, price):
        """
        __init__: Constructor method - called when object is created.
        This is the most common magic method!
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        """
        __str__: Returns user-friendly string representation.
        Called by str() and print().
        Should be readable and informative.
        """
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """
        __repr__: Returns developer-friendly string representation.
        Called by repr() and in interactive shell.
        Should be unambiguous and ideally show how to recreate the object.
        """
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages}, price={self.price})"


def demo_initialization_and_representation():
    """Demonstrate __init__, __str__, and __repr__."""
    print("\n" + "="*60)
    print("INITIALIZATION AND REPRESENTATION")
    print("="*60)

    book = Book("Python Mastery", "Alice Johnson", 450, 39.99)

    print(f"\nCreated book object:")
    print(f"  str(book):  {str(book)}")           # Calls __str__
    print(f"  repr(book): {repr(book)}")          # Calls __repr__
    print(f"  print(book): ", end="")
    print(book)                                    # Calls __str__

    # In interactive shell or debugging
    print(f"\n  In shell: {book!r}")              # Uses __repr__


# =============================================================================
# 2. COMPARISON OPERATORS
# =============================================================================

class Product:
    """Product class with comparison operators."""

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def __eq__(self, other):
        """
        __eq__: Equality comparison (==)
        Returns True if objects are considered equal.
        """
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price and self.name == other.name

    def __lt__(self, other):
        """
        __lt__: Less than comparison (<)
        Used for sorting and ordering.
        """
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        """__le__: Less than or equal (<=)"""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price <= other.price

    def __gt__(self, other):
        """__gt__: Greater than (>)"""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __ge__(self, other):
        """__ge__: Greater than or equal (>=)"""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price >= other.price

    def __ne__(self, other):
        """
        __ne__: Not equal (!=)
        Python automatically provides this if __eq__ is defined,
        but you can override it if needed.
        """
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.name} (${self.price:.2f}, Rating: {self.rating}/5)"


def demo_comparison_operators():
    """Demonstrate comparison magic methods."""
    print("\n" + "="*60)
    print("COMPARISON OPERATORS")
    print("="*60)

    laptop = Product("Laptop", 999.99, 4.5)
    phone = Product("Phone", 699.99, 4.8)
    tablet = Product("Tablet", 699.99, 4.3)

    print(f"\nProducts:")
    print(f"  {laptop}")
    print(f"  {phone}")
    print(f"  {tablet}")

    print(f"\nComparisons:")
    print(f"  laptop == phone: {laptop == phone}")
    print(f"  phone == tablet: {phone == tablet}")  # Same price, different name
    print(f"  laptop > phone: {laptop > phone}")
    print(f"  phone < laptop: {phone < laptop}")
    print(f"  phone <= tablet: {phone <= tablet}")

    # Sorting works because we defined __lt__
    products = [laptop, phone, tablet]
    products.sort()
    print(f"\nSorted by price:")
    for p in products:
        print(f"  {p}")


# =============================================================================
# 3. ARITHMETIC OPERATORS
# =============================================================================

class Money:
    """Money class with arithmetic operations."""

    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        """
        __add__: Addition operator (+)
        Allows: money1 + money2
        """
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot add different currencies")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented

    def __sub__(self, other):
        """__sub__: Subtraction operator (-)"""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot subtract different currencies")
            return Money(self.amount - other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency)
        return NotImplemented

    def __mul__(self, other):
        """
        __mul__: Multiplication operator (*)
        Allows: money * number
        """
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        return NotImplemented

    def __truediv__(self, other):
        """__truediv__: Division operator (/)"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero")
            return Money(self.amount / other, self.currency)
        return NotImplemented

    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"


def demo_arithmetic_operators():
    """Demonstrate arithmetic magic methods."""
    print("\n" + "="*60)
    print("ARITHMETIC OPERATORS")
    print("="*60)

    price1 = Money(100.50)
    price2 = Money(49.99)
    discount = Money(10.00)

    print(f"\nMoney objects:")
    print(f"  price1 = {price1}")
    print(f"  price2 = {price2}")
    print(f"  discount = {discount}")

    print(f"\nArithmetic operations:")
    print(f"  price1 + price2 = {price1 + price2}")
    print(f"  price1 - discount = {price1 - discount}")
    print(f"  price2 * 2 = {price2 * 2}")
    print(f"  price1 / 2 = {price1 / 2}")

    # Chaining operations
    total = (price1 + price2 - discount) * 1.1  # Add 10% tax
    print(f"  (price1 + price2 - discount) * 1.1 = {total}")


# =============================================================================
# 4. CONTAINER METHODS (__len__, __getitem__, __setitem__, __contains__)
# =============================================================================

class Playlist:
    """Playlist class behaving like a container."""

    def __init__(self, name):
        self.name = name
        self._songs = []

    def add_song(self, song):
        """Add a song to the playlist."""
        self._songs.append(song)

    def __len__(self):
        """
        __len__: Returns length of container.
        Allows: len(playlist)
        """
        return len(self._songs)

    def __getitem__(self, index):
        """
        __getitem__: Get item by index or slice.
        Allows: playlist[0], playlist[1:3], for song in playlist
        Makes object iterable!
        """
        return self._songs[index]

    def __setitem__(self, index, value):
        """
        __setitem__: Set item by index.
        Allows: playlist[0] = "New Song"
        """
        self._songs[index] = value

    def __contains__(self, song):
        """
        __contains__: Check if item exists.
        Allows: "song" in playlist
        """
        return song in self._songs

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"


def demo_container_methods():
    """Demonstrate container magic methods."""
    print("\n" + "="*60)
    print("CONTAINER METHODS")
    print("="*60)

    playlist = Playlist("My Favorites")
    playlist.add_song("Bohemian Rhapsody")
    playlist.add_song("Hotel California")
    playlist.add_song("Stairway to Heaven")
    playlist.add_song("Imagine")

    print(f"\n{playlist}")

    # __len__
    print(f"\nNumber of songs: {len(playlist)}")

    # __getitem__
    print(f"First song: {playlist[0]}")
    print(f"Last song: {playlist[-1]}")
    print(f"Songs 1-2: {playlist[1:3]}")

    # __setitem__
    print(f"\nChanging second song...")
    playlist[1] = "Sweet Child O' Mine"
    print(f"Second song is now: {playlist[1]}")

    # __contains__
    print(f"\nIs 'Imagine' in playlist? {'Imagine' in playlist}")
    print(f"Is 'Yesterday' in playlist? {'Yesterday' in playlist}")

    # __getitem__ makes it iterable!
    print(f"\nAll songs:")
    for i, song in enumerate(playlist, 1):
        print(f"  {i}. {song}")


# =============================================================================
# 5. CALLABLE OBJECTS (__call__)
# =============================================================================

class Multiplier:
    """Class that can be called like a function."""

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """
        __call__: Makes instance callable like a function.
        Allows: obj(arguments)
        """
        return x * self.factor

    def __str__(self):
        return f"Multiplier(factor={self.factor})"


class Logger:
    """Logger that counts calls."""

    def __init__(self, prefix="LOG"):
        self.prefix = prefix
        self.call_count = 0

    def __call__(self, message):
        """Make logger callable."""
        self.call_count += 1
        print(f"[{self.prefix} #{self.call_count}] {message}")

    def get_stats(self):
        return f"Logger called {self.call_count} times"


def demo_callable_objects():
    """Demonstrate __call__ magic method."""
    print("\n" + "="*60)
    print("CALLABLE OBJECTS")
    print("="*60)

    # Multiplier example
    print(f"\nMultiplier example:")
    double = Multiplier(2)
    triple = Multiplier(3)

    print(f"  double = {double}")
    print(f"  double(5) = {double(5)}")      # Calling object like function!
    print(f"  double(10) = {double(10)}")
    print(f"  triple(5) = {triple(5)}")

    # Logger example
    print(f"\nLogger example:")
    logger = Logger("INFO")
    logger("Application started")              # Calling object!
    logger("User logged in")
    logger("Database connection established")
    print(f"  {logger.get_stats()}")


# =============================================================================
# 6. CONTEXT MANAGERS (__enter__, __exit__)
# =============================================================================

class DatabaseConnection:
    """Database connection using context manager protocol."""

    def __init__(self, database_name):
        self.database_name = database_name
        self.connected = False

    def __enter__(self):
        """
        __enter__: Called when entering 'with' block.
        Should return the resource to be used.
        Allows: with DatabaseConnection("mydb") as conn:
        """
        print(f"  Opening connection to {self.database_name}...")
        self.connected = True
        return self  # Return self to use in 'as' clause

    def __exit__(self, exc_type, exc_value, traceback):
        """
        __exit__: Called when exiting 'with' block.
        Guaranteed to be called even if exception occurs!

        Parameters:
        - exc_type: Exception type (if exception occurred)
        - exc_value: Exception value
        - traceback: Traceback object

        Return True to suppress exception, False to propagate it.
        """
        print(f"  Closing connection to {self.database_name}...")
        self.connected = False

        if exc_type is not None:
            print(f"  Exception occurred: {exc_type.__name__}: {exc_value}")
            # Return False to propagate exception
            return False

        return True

    def query(self, sql):
        """Execute a query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        return f"Query executed: {sql}"


class Timer:
    """Timer context manager to measure execution time."""

    def __init__(self, description="Code block"):
        self.description = description
        self.start_time = None
        self.elapsed_time = None

    def __enter__(self):
        """Start timing."""
        import time
        self.start_time = time.time()
        print(f"  Starting: {self.description}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Stop timing."""
        import time
        self.elapsed_time = time.time() - self.start_time
        print(f"  Finished: {self.description} (took {self.elapsed_time:.4f} seconds)")
        return False  # Don't suppress exceptions


def demo_context_managers():
    """Demonstrate context manager magic methods."""
    print("\n" + "="*60)
    print("CONTEXT MANAGERS")
    print("="*60)

    # Database connection example
    print(f"\nDatabase connection example:")
    with DatabaseConnection("users_db") as db:
        result = db.query("SELECT * FROM users")
        print(f"  {result}")
    # Connection automatically closed when exiting 'with' block!

    # Timer example
    print(f"\nTimer example:")
    with Timer("Data processing"):
        # Simulate some work
        total = sum(range(1000000))
        print(f"    Calculated sum: {total}")

    # Context manager with exception
    print(f"\nContext manager with exception:")
    try:
        with DatabaseConnection("test_db") as db:
            print(f"  Working with database...")
            raise ValueError("Something went wrong!")
    except ValueError as e:
        print(f"  Caught exception: {e}")
    # Connection still closed properly!


# =============================================================================
# 7. REAL-WORLD EXAMPLE: Advanced Shopping Cart
# =============================================================================

class CartItem:
    """Individual item in shopping cart."""

    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} x{self.quantity} @ ${self.price:.2f} = ${self.total():.2f}"

    def __repr__(self):
        return f"CartItem({self.name!r}, {self.price}, {self.quantity})"

    def __eq__(self, other):
        """Items are equal if they have the same name."""
        if not isinstance(other, CartItem):
            return NotImplemented
        return self.name == other.name

    def total(self):
        return self.price * self.quantity


class ShoppingCart:
    """Shopping cart with comprehensive magic methods."""

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self._items = []

    def add_item(self, item):
        """Add item to cart."""
        # If item already exists, increase quantity
        for cart_item in self._items:
            if cart_item == item:
                cart_item.quantity += item.quantity
                return
        self._items.append(item)

    def __len__(self):
        """Total number of items (counting quantities)."""
        return sum(item.quantity for item in self._items)

    def __getitem__(self, index):
        """Get item by index."""
        return self._items[index]

    def __contains__(self, item_name):
        """Check if item exists in cart."""
        return any(item.name == item_name for item in self._items)

    def __add__(self, other):
        """Merge two shopping carts."""
        if not isinstance(other, ShoppingCart):
            return NotImplemented

        new_cart = ShoppingCart(f"{self.customer_name} + {other.customer_name}")
        new_cart._items = self._items.copy()

        for item in other._items:
            new_cart.add_item(CartItem(item.name, item.price, item.quantity))

        return new_cart

    def __str__(self):
        """User-friendly representation."""
        if not self._items:
            return f"Shopping cart for {self.customer_name} is empty"

        lines = [f"Shopping cart for {self.customer_name}:"]
        for item in self._items:
            lines.append(f"  - {item}")
        lines.append(f"  Total: ${self.total():.2f} ({len(self)} items)")
        return "\n".join(lines)

    def __repr__(self):
        return f"ShoppingCart({self.customer_name!r}, items={len(self._items)})"

    def __call__(self, discount_percent=0):
        """Make cart callable to apply discount."""
        total = self.total()
        discount = total * (discount_percent / 100)
        final = total - discount
        return f"Total: ${total:.2f} - Discount {discount_percent}%: ${discount:.2f} = ${final:.2f}"

    def total(self):
        """Calculate total cost."""
        return sum(item.total() for item in self._items)


def demo_shopping_cart():
    """Demonstrate comprehensive magic methods."""
    print("\n" + "="*60)
    print("REAL-WORLD EXAMPLE: Advanced Shopping Cart")
    print("="*60)

    # Create cart and add items
    cart1 = ShoppingCart("Alice")
    cart1.add_item(CartItem("Laptop", 999.99))
    cart1.add_item(CartItem("Mouse", 29.99, 2))
    cart1.add_item(CartItem("Keyboard", 79.99))

    # __str__
    print(f"\n{cart1}")

    # __len__
    print(f"\nTotal items in cart: {len(cart1)}")

    # __contains__
    print(f"Is 'Laptop' in cart? {'Laptop' in cart1}")
    print(f"Is 'Monitor' in cart? {'Monitor' in cart1}")

    # __getitem__ - iteration
    print(f"\nIterating through cart:")
    for item in cart1:
        print(f"  {item.name}: ${item.total():.2f}")

    # __call__ - apply discount
    print(f"\n{cart1(10)}")  # 10% discount
    print(f"{cart1(20)}")     # 20% discount

    # __add__ - merge carts
    cart2 = ShoppingCart("Bob")
    cart2.add_item(CartItem("Monitor", 299.99))
    cart2.add_item(CartItem("Mouse", 29.99))  # Same as in cart1

    print(f"\nBob's cart:")
    print(f"{cart2}")

    merged = cart1 + cart2
    print(f"\nMerged cart:")
    print(f"{merged}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

def print_key_takeaways():
    """Print key learning points."""
    print("\n" + "="*60)
    print("KEY TAKEAWAYS - Magic Methods")
    print("="*60)

    takeaways = [
        "1. Magic methods start and end with double underscores (__method__)",
        "2. __init__: Initialize objects, __str__: user display, __repr__: dev display",
        "3. Comparison: __eq__, __lt__, __le__, __gt__, __ge__, __ne__",
        "4. Arithmetic: __add__, __sub__, __mul__, __truediv__, __mod__",
        "5. Container: __len__, __getitem__, __setitem__, __contains__",
        "6. __call__: Makes objects callable like functions",
        "7. Context managers: __enter__ and __exit__ for resource management",
        "8. Magic methods make objects behave like built-in types"
    ]

    for takeaway in takeaways:
        print(f"  {takeaway}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*60)
    print("LESSON 7: MAGIC METHODS IN PYTHON")
    print("="*60)

    # Run all demonstrations
    demo_initialization_and_representation()
    demo_comparison_operators()
    demo_arithmetic_operators()
    demo_container_methods()
    demo_callable_objects()
    demo_context_managers()
    demo_shopping_cart()
    print_key_takeaways()

    print("\n" + "="*60)
    print("LESSON COMPLETE!")
    print("="*60)
    print("\nNext: Lesson 8 - Properties")
    print("Run: python lessons/08_properties.py")
