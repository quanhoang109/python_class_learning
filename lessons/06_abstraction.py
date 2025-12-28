"""
Lesson 6: Abstraction in Python
================================

Abstraction is the process of hiding complex implementation details
and showing only the essential features of an object.

Key Concepts:
1. Abstract Base Classes (ABC)
2. Abstract Methods
3. Interface-like behavior
4. Hiding implementation complexity

Run this file: python lessons/06_abstraction.py
"""

from abc import ABC, abstractmethod
from datetime import datetime


# =============================================================================
# 1. ABSTRACT BASE CLASSES - Cannot be instantiated directly
# =============================================================================

class Vehicle(ABC):
    """
    Abstract base class for vehicles.
    Cannot create a Vehicle object directly - must create a specific type.
    """

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    @abstractmethod
    def start_engine(self):
        """Abstract method - must be implemented by child classes."""
        pass

    @abstractmethod
    def stop_engine(self):
        """Abstract method - must be implemented by child classes."""
        pass

    @abstractmethod
    def get_fuel_type(self):
        """Abstract method - must be implemented by child classes."""
        pass

    def honk(self):
        """Concrete method - shared by all vehicles."""
        return "Beep beep!"


class Car(Vehicle):
    """Concrete class - implements all abstract methods."""

    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model}: Engine started with key ignition"

    def stop_engine(self):
        self.is_running = False
        return f"{self.brand} {self.model}: Engine stopped"

    def get_fuel_type(self):
        return "Gasoline"


class ElectricCar(Vehicle):
    """Electric car - different implementation."""

    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model}: Electric motor activated silently"

    def stop_engine(self):
        self.is_running = False
        return f"{self.brand} {self.model}: Electric motor deactivated"

    def get_fuel_type(self):
        return f"Electric (Battery: {self.battery_capacity}kWh)"


class Motorcycle(Vehicle):
    """Motorcycle - yet another implementation."""

    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model}: Motorcycle engine roars to life!"

    def stop_engine(self):
        self.is_running = False
        return f"{self.brand} {self.model}: Engine silenced"

    def get_fuel_type(self):
        return "Gasoline (Premium)"


def demo_abstract_classes():
    """Demonstrate abstract base classes."""
    print("\n" + "="*60)
    print("ABSTRACT BASE CLASSES")
    print("="*60)

    # Try to create abstract class (uncomment to see error)
    # vehicle = Vehicle("Generic", "Model", 2024)  # TypeError!

    # Create concrete classes
    vehicles = [
        Car("Toyota", "Camry", 2024),
        ElectricCar("Tesla", "Model 3", 2024, 75),
        Motorcycle("Harley-Davidson", "Street 750", 2024)
    ]

    for vehicle in vehicles:
        print(f"\n{vehicle.__class__.__name__}: {vehicle.brand} {vehicle.model}")
        print(f"  {vehicle.start_engine()}")
        print(f"  Fuel Type: {vehicle.get_fuel_type()}")
        print(f"  {vehicle.honk()}")
        print(f"  {vehicle.stop_engine()}")


# =============================================================================
# 2. INTERFACE-LIKE ABSTRACTION - Define contracts
# =============================================================================

class DatabaseInterface(ABC):
    """
    Interface for database operations.
    Defines WHAT operations must exist, not HOW they work.
    """

    @abstractmethod
    def connect(self):
        """Connect to database."""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnect from database."""
        pass

    @abstractmethod
    def query(self, sql):
        """Execute a query."""
        pass

    @abstractmethod
    def insert(self, table, data):
        """Insert data."""
        pass


class MySQLDatabase(DatabaseInterface):
    """MySQL implementation - hides MySQL-specific complexity."""

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.connected = False

    def connect(self):
        """MySQL connection implementation."""
        self.connected = True
        return f"Connected to MySQL at {self.host}:{self.port}"

    def disconnect(self):
        """MySQL disconnection implementation."""
        self.connected = False
        return "Disconnected from MySQL"

    def query(self, sql):
        """Execute MySQL query."""
        if not self.connected:
            return "Error: Not connected"
        return f"MySQL Query executed: {sql}"

    def insert(self, table, data):
        """Insert into MySQL."""
        if not self.connected:
            return "Error: Not connected"
        return f"Inserted into MySQL table '{table}': {data}"


class PostgreSQLDatabase(DatabaseInterface):
    """PostgreSQL implementation - different internal workings."""

    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connected = False

    def connect(self):
        """PostgreSQL connection implementation."""
        self.connected = True
        return f"Connected to PostgreSQL database '{self.database}' at {self.host}"

    def disconnect(self):
        """PostgreSQL disconnection implementation."""
        self.connected = False
        return "Disconnected from PostgreSQL"

    def query(self, sql):
        """Execute PostgreSQL query."""
        if not self.connected:
            return "Error: Not connected"
        return f"PostgreSQL Query executed: {sql}"

    def insert(self, table, data):
        """Insert into PostgreSQL."""
        if not self.connected:
            return "Error: Not connected"
        return f"Inserted into PostgreSQL table '{table}': {data}"


class MongoDBDatabase(DatabaseInterface):
    """MongoDB implementation - NoSQL but same interface."""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False

    def connect(self):
        """MongoDB connection implementation."""
        self.connected = True
        return f"Connected to MongoDB: {self.connection_string}"

    def disconnect(self):
        """MongoDB disconnection implementation."""
        self.connected = False
        return "Disconnected from MongoDB"

    def query(self, sql):
        """MongoDB doesn't use SQL, but we adapt."""
        if not self.connected:
            return "Error: Not connected"
        return f"MongoDB Query (translated from SQL): {sql}"

    def insert(self, table, data):
        """Insert into MongoDB collection."""
        if not self.connected:
            return "Error: Not connected"
        return f"Inserted into MongoDB collection '{table}': {data}"


def use_database(db: DatabaseInterface):
    """
    This function works with ANY database that implements DatabaseInterface.
    It doesn't care about the internal implementation - abstraction!
    """
    print(db.connect())
    print(db.query("SELECT * FROM users"))
    print(db.insert("users", {"name": "Alice", "age": 30}))
    print(db.disconnect())


def demo_interface_abstraction():
    """Demonstrate interface-like abstraction."""
    print("\n" + "="*60)
    print("INTERFACE-LIKE ABSTRACTION")
    print("="*60)

    databases = [
        MySQLDatabase("localhost", 3306, "user", "pass"),
        PostgreSQLDatabase("localhost", "myapp"),
        MongoDBDatabase("mongodb://localhost:27017")
    ]

    for db in databases:
        print(f"\n--- Using {db.__class__.__name__} ---")
        use_database(db)


# =============================================================================
# 3. HIDING COMPLEXITY - Real-world example
# =============================================================================

class NotificationService(ABC):
    """
    Abstract notification service.
    Hides the complexity of different notification methods.
    """

    @abstractmethod
    def send(self, recipient, message):
        """Send a notification."""
        pass

    @abstractmethod
    def validate_recipient(self, recipient):
        """Validate recipient format."""
        pass


class EmailNotification(NotificationService):
    """Email notification - complex SMTP logic hidden."""

    def validate_recipient(self, recipient):
        """Validate email address."""
        return "@" in recipient and "." in recipient

    def send(self, recipient, message):
        """Send email (simplified - real implementation would use SMTP)."""
        if not self.validate_recipient(recipient):
            return f"Error: Invalid email address '{recipient}'"

        # In reality, this would connect to SMTP server,
        # handle authentication, format MIME message, etc.
        # All that complexity is HIDDEN from the user!
        return f"Email sent to {recipient}: {message}"


class SMSNotification(NotificationService):
    """SMS notification - complex telecom API logic hidden."""

    def validate_recipient(self, recipient):
        """Validate phone number."""
        return recipient.replace("-", "").replace("+", "").isdigit()

    def send(self, recipient, message):
        """Send SMS (simplified - real implementation would use Twilio, etc.)."""
        if not self.validate_recipient(recipient):
            return f"Error: Invalid phone number '{recipient}'"

        # In reality, this would connect to SMS gateway,
        # handle rate limiting, retries, delivery reports, etc.
        # All that complexity is HIDDEN!
        return f"SMS sent to {recipient}: {message}"


class PushNotification(NotificationService):
    """Push notification - complex mobile platform logic hidden."""

    def validate_recipient(self, recipient):
        """Validate device token."""
        return len(recipient) > 20  # Simplified validation

    def send(self, recipient, message):
        """Send push notification."""
        if not self.validate_recipient(recipient):
            return f"Error: Invalid device token '{recipient}'"

        # In reality, this would connect to Firebase/APNS,
        # handle device registration, badges, sounds, etc.
        # All that complexity is HIDDEN!
        return f"Push notification sent to device {recipient[:10]}...: {message}"


class NotificationManager:
    """
    High-level notification manager.
    Users don't need to know HOW notifications are sent,
    just that they ARE sent. Maximum abstraction!
    """

    def __init__(self):
        self.services = {
            'email': EmailNotification(),
            'sms': SMSNotification(),
            'push': PushNotification()
        }

    def notify(self, method, recipient, message):
        """
        Send notification using specified method.
        All complexity is abstracted away!
        """
        if method not in self.services:
            return f"Error: Unknown notification method '{method}'"

        service = self.services[method]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {service.send(recipient, message)}")


def demo_hiding_complexity():
    """Demonstrate hiding complexity through abstraction."""
    print("\n" + "="*60)
    print("HIDING COMPLEXITY")
    print("="*60)

    # User doesn't need to know ANYTHING about SMTP, SMS gateways, or push services
    # They just use a simple interface!
    manager = NotificationManager()

    print("\nSending notifications (complexity hidden):\n")
    manager.notify('email', 'user@example.com', 'Welcome to our service!')
    manager.notify('sms', '+1-555-0123', 'Your verification code is 123456')
    manager.notify('push', 'device_token_abc123xyz789', 'You have a new message!')
    manager.notify('email', 'invalid-email', 'This will fail validation')


# =============================================================================
# 4. REAL-WORLD EXAMPLE: File Storage Abstraction
# =============================================================================

class FileStorage(ABC):
    """Abstract file storage - local, cloud, etc."""

    @abstractmethod
    def upload(self, filename, content):
        """Upload a file."""
        pass

    @abstractmethod
    def download(self, filename):
        """Download a file."""
        pass

    @abstractmethod
    def delete(self, filename):
        """Delete a file."""
        pass

    @abstractmethod
    def list_files(self):
        """List all files."""
        pass


class LocalStorage(FileStorage):
    """Local filesystem storage."""

    def __init__(self, base_path):
        self.base_path = base_path
        self.files = {}  # Simplified in-memory storage for demo

    def upload(self, filename, content):
        self.files[filename] = content
        return f"Uploaded '{filename}' to local storage at {self.base_path}"

    def download(self, filename):
        if filename in self.files:
            return f"Downloaded '{filename}' from local storage: {self.files[filename]}"
        return f"Error: File '{filename}' not found"

    def delete(self, filename):
        if filename in self.files:
            del self.files[filename]
            return f"Deleted '{filename}' from local storage"
        return f"Error: File '{filename}' not found"

    def list_files(self):
        return list(self.files.keys())


class S3Storage(FileStorage):
    """AWS S3 cloud storage."""

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.files = {}  # Simplified for demo

    def upload(self, filename, content):
        # Real implementation would use boto3 library
        self.files[filename] = content
        return f"Uploaded '{filename}' to S3 bucket '{self.bucket_name}'"

    def download(self, filename):
        if filename in self.files:
            return f"Downloaded '{filename}' from S3: {self.files[filename]}"
        return f"Error: File '{filename}' not found in S3"

    def delete(self, filename):
        if filename in self.files:
            del self.files[filename]
            return f"Deleted '{filename}' from S3 bucket '{self.bucket_name}'"
        return f"Error: File '{filename}' not found"

    def list_files(self):
        return list(self.files.keys())


class Application:
    """
    Application that uses file storage.
    It doesn't care WHERE files are stored - complete abstraction!
    """

    def __init__(self, storage: FileStorage):
        self.storage = storage

    def save_user_data(self, username, data):
        """Save user data - storage location abstracted."""
        filename = f"{username}_data.txt"
        return self.storage.upload(filename, data)

    def load_user_data(self, username):
        """Load user data - storage location abstracted."""
        filename = f"{username}_data.txt"
        return self.storage.download(filename)

    def show_all_files(self):
        """Show all files."""
        files = self.storage.list_files()
        return f"Files in storage: {', '.join(files) if files else 'None'}"


def demo_file_storage_abstraction():
    """Demonstrate file storage abstraction."""
    print("\n" + "="*60)
    print("FILE STORAGE ABSTRACTION")
    print("="*60)

    # Same application code works with different storage backends!
    print("\n--- Using Local Storage ---")
    local_app = Application(LocalStorage("/var/data"))
    print(local_app.save_user_data("alice", "Alice's preferences"))
    print(local_app.save_user_data("bob", "Bob's settings"))
    print(local_app.show_all_files())
    print(local_app.load_user_data("alice"))

    print("\n--- Using S3 Cloud Storage ---")
    cloud_app = Application(S3Storage("my-app-bucket"))
    print(cloud_app.save_user_data("charlie", "Charlie's data"))
    print(cloud_app.save_user_data("diana", "Diana's config"))
    print(cloud_app.show_all_files())
    print(cloud_app.load_user_data("charlie"))


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

def print_key_takeaways():
    """Print key learning points."""
    print("\n" + "="*60)
    print("KEY TAKEAWAYS - Abstraction")
    print("="*60)

    takeaways = [
        "1. Abstraction = Hide complexity, show only essentials",
        "2. Abstract Base Classes: Define what subclasses MUST implement",
        "3. Cannot instantiate abstract classes directly",
        "4. Interfaces: Define contracts (what, not how)",
        "5. Benefits: Simpler code, easier to change implementations",
        "6. Real-world: Databases, notifications, storage all use abstraction"
    ]

    for takeaway in takeaways:
        print(f"  ✓ {takeaway}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*60)
    print("LESSON 6: ABSTRACTION IN PYTHON")
    print("="*60)

    # Run all demonstrations
    demo_abstract_classes()
    demo_interface_abstraction()
    demo_hiding_complexity()
    demo_file_storage_abstraction()
    print_key_takeaways()

    print("\n" + "="*60)
    print("LESSON COMPLETE!")
    print("="*60)
    print("\nNext: Lesson 7 - Magic Methods")
    print("Run: python lessons/07_magic_methods.py")
