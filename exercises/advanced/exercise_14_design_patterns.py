"""
Exercise 14: Design Patterns Practice

Implement common design patterns in a real-world scenario:
An E-Commerce Order Processing System

┌─────────────────────────────────────────────────────────────────────┐
│ DESIGN PATTERNS TO IMPLEMENT                                        │
├─────────────────────────────────────────────────────────────────────┤
│ 1. STRATEGY PATTERN      - Different payment methods                │
│ 2. OBSERVER PATTERN      - Order status notifications               │
│ 3. FACTORY PATTERN       - Create different product types           │
│ 4. SINGLETON PATTERN     - Application configuration                │
│ 5. DECORATOR PATTERN     - Add features to products (gift wrap)     │
└─────────────────────────────────────────────────────────────────────┘

Scenario: Build an order processing system with:
- Multiple payment methods (Credit Card, PayPal, Crypto)
- Order status updates that notify multiple services
- Product creation through a factory
- Single configuration instance
- Product decorators for gift wrapping, insurance, etc.

"""

from abc import ABC, abstractmethod
from datetime import datetime


# =============================================================================
# 1. STRATEGY PATTERN - Payment Methods
# =============================================================================
# Different payment strategies that can be swapped at runtime

class PaymentStrategy(ABC):
    """Abstract payment strategy."""

    @abstractmethod
    def pay(self, amount):
        """Process payment and return confirmation."""
        pass

    @abstractmethod
    def get_fee(self, amount):
        """Calculate processing fee."""
        pass


class CreditCardPayment(PaymentStrategy):
    """Credit card payment strategy."""

    def __init__(self, card_number, cvv, expiry):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def pay(self, amount):
        # TODO: Implement
        
        pass

    def get_fee(self, amount):
        # 2.5% fee
        # TODO: Implement
        pass


class PayPalPayment(PaymentStrategy):
    """PayPal payment strategy."""

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        # TODO: Implement
        pass

    def get_fee(self, amount):
        # 3% fee
        # TODO: Implement
        pass


class CryptoPayment(PaymentStrategy):
    """Cryptocurrency payment strategy."""

    def __init__(self, wallet_address, crypto_type="BTC"):
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type

    def pay(self, amount):
        # TODO: Implement
        pass

    def get_fee(self, amount):
        # 1% fee
        # TODO: Implement
        pass


# =============================================================================
# 2. OBSERVER PATTERN - Order Status Notifications
# =============================================================================
# When order status changes, notify all registered observers

class OrderObserver(ABC):
    """Abstract observer for order updates."""

    @abstractmethod
    def update(self, order, old_status, new_status):
        """Called when order status changes."""
        pass


class EmailNotifier(OrderObserver):
    """Sends email notifications."""

    def update(self, order, old_status, new_status):
        # TODO: Implement
        pass


class SMSNotifier(OrderObserver):
    """Sends SMS notifications."""

    def update(self, order, old_status, new_status):
        # TODO: Implement
        pass


class InventoryManager(OrderObserver):
    """Updates inventory when order status changes."""

    def update(self, order, old_status, new_status):
        # TODO: Implement - e.g., reserve items when CONFIRMED, release when CANCELLED
        pass


class AnalyticsTracker(OrderObserver):
    """Tracks order analytics."""

    def update(self, order, old_status, new_status):
        # TODO: Implement
        pass


class Order:
    """Order class that notifies observers on status change."""

    STATUSES = ["PENDING", "CONFIRMED", "PROCESSING", "SHIPPED", "DELIVERED", "CANCELLED"]

    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
        self._status = "PENDING"
        self._observers = []
        self.created_at = datetime.now()

    def attach(self, observer):
        """Attach an observer."""
        # TODO: Implement
        pass

    def detach(self, observer):
        """Detach an observer."""
        # TODO: Implement
        pass

    def _notify_observers(self, old_status, new_status):
        """Notify all observers of status change."""
        # TODO: Implement
        pass

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        """Set status and notify observers."""
        # TODO: Implement - validate status and notify observers
        pass

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        return sum(item.get_price() for item in self.items)


# =============================================================================
# 3. FACTORY PATTERN - Product Creation
# =============================================================================
# Create different product types without specifying exact class

class Product(ABC):
    """Abstract product."""

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def get_price(self):
        """Get the final price."""
        pass

    @abstractmethod
    def get_description(self):
        """Get product description."""
        pass


class Electronics(Product):
    """Electronics product with warranty."""

    def __init__(self, name, base_price, warranty_years=1):
        super().__init__(name, base_price)
        self.warranty_years = warranty_years

    def get_price(self):
        # TODO: Implement
        pass

    def get_description(self):
        # TODO: Implement
        pass


class Clothing(Product):
    """Clothing product with size."""

    def __init__(self, name, base_price, size, material):
        super().__init__(name, base_price)
        self.size = size
        self.material = material

    def get_price(self):
        # TODO: Implement
        pass

    def get_description(self):
        # TODO: Implement
        pass


class Food(Product):
    """Food product with expiry."""

    def __init__(self, name, base_price, expiry_days):
        super().__init__(name, base_price)
        self.expiry_days = expiry_days

    def get_price(self):
        # TODO: Implement
        pass

    def get_description(self):
        # TODO: Implement
        pass


class ProductFactory:
    """Factory for creating products."""

    @staticmethod
    def create_product(product_type, name, base_price, **kwargs):
        """
        Create a product based on type.

        Args:
            product_type: "electronics", "clothing", or "food"
            name: Product name
            base_price: Base price
            **kwargs: Additional arguments for specific product types
        """
        # TODO: Implement factory logic
        pass


# =============================================================================
# 4. SINGLETON PATTERN - Configuration
# =============================================================================
# Only one instance of configuration should exist

class ConfigurationMeta(type):
    """Metaclass for Singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # TODO: Implement singleton logic
        pass


class Configuration(metaclass=ConfigurationMeta):
    """Application configuration - Singleton."""

    def __init__(self):
        # Only initialize once
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.settings = {
                "currency": "USD",
                "tax_rate": 0.08,
                "free_shipping_threshold": 50,
                "max_items_per_order": 100
            }

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value


# =============================================================================
# 5. DECORATOR PATTERN - Product Add-ons
# =============================================================================
# Add features to products dynamically

class ProductDecorator(Product):
    """Base decorator for products."""

    def __init__(self, product):
        self._product = product

    @property
    def name(self):
        return self._product.name

    @property
    def base_price(self):
        return self._product.base_price


class GiftWrap(ProductDecorator):
    """Adds gift wrapping to product."""

    GIFT_WRAP_COST = 5.99

    def get_price(self):
        # TODO: Implement - add gift wrap cost
        pass

    def get_description(self):
        # TODO: Implement - add gift wrap to description
        pass


class Insurance(ProductDecorator):
    """Adds insurance to product."""

    INSURANCE_RATE = 0.10  # 10% of product price

    def get_price(self):
        # TODO: Implement - add insurance cost
        pass

    def get_description(self):
        # TODO: Implement - add insurance to description
        pass


class ExpressShipping(ProductDecorator):
    """Adds express shipping to product."""

    EXPRESS_COST = 15.00

    def get_price(self):
        # TODO: Implement
        pass

    def get_description(self):
        # TODO: Implement
        pass


# =============================================================================
# ORDER PROCESSOR - Combines all patterns
# =============================================================================

class OrderProcessor:
    """Processes orders using all the patterns."""

    def __init__(self):
        self.config = Configuration()

    def create_order(self, order_id, customer_name):
        """Create a new order with observers attached."""
        order = Order(order_id, customer_name)

        # Attach default observers
        order.attach(EmailNotifier())
        order.attach(InventoryManager())
        order.attach(AnalyticsTracker())

        return order

    def process_payment(self, order, payment_strategy):
        """Process payment using the given strategy."""
        total = order.get_total()
        fee = payment_strategy.get_fee(total)
        final_amount = total + fee

        result = payment_strategy.pay(final_amount)

        if result:
            order.status = "CONFIRMED"

        return result, final_amount

    def add_product_to_order(self, order, product_type, name, price, **kwargs):
        """Add product to order using factory."""
        product = ProductFactory.create_product(product_type, name, price, **kwargs)
        order.add_item(product)
        return product


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DESIGN PATTERNS - E-COMMERCE SYSTEM TESTS")
    print("=" * 60)

    # TODO: Uncomment tests after implementing patterns

    # # Test 1: Singleton Pattern
    # print("\n--- Test 1: Singleton Pattern (Configuration) ---")
    # config1 = Configuration()
    # config2 = Configuration()
    # print(f"Same instance? {config1 is config2}")
    # config1.set("currency", "EUR")
    # print(f"Config2 sees change? {config2.get('currency')}")

    # # Test 2: Factory Pattern
    # print("\n--- Test 2: Factory Pattern (Products) ---")
    # laptop = ProductFactory.create_product("electronics", "Laptop", 999, warranty_years=2)
    # shirt = ProductFactory.create_product("clothing", "T-Shirt", 29.99, size="M", material="Cotton")
    # apple = ProductFactory.create_product("food", "Organic Apple", 2.99, expiry_days=7)
    # print(f"Laptop: {laptop.get_description()} - ${laptop.get_price()}")
    # print(f"Shirt: {shirt.get_description()} - ${shirt.get_price()}")
    # print(f"Apple: {apple.get_description()} - ${apple.get_price()}")

    # # Test 3: Decorator Pattern
    # print("\n--- Test 3: Decorator Pattern (Add-ons) ---")
    # basic_laptop = ProductFactory.create_product("electronics", "Laptop", 999)
    # print(f"Basic: {basic_laptop.get_description()} - ${basic_laptop.get_price()}")
    #
    # wrapped_laptop = GiftWrap(basic_laptop)
    # print(f"Gift wrapped: {wrapped_laptop.get_description()} - ${wrapped_laptop.get_price()}")
    #
    # insured_wrapped = Insurance(wrapped_laptop)
    # print(f"+ Insurance: {insured_wrapped.get_description()} - ${insured_wrapped.get_price()}")

    # # Test 4: Strategy Pattern
    # print("\n--- Test 4: Strategy Pattern (Payments) ---")
    # amount = 100
    #
    # cc = CreditCardPayment("4111111111111111", "123", "12/25")
    # print(f"Credit Card fee on ${amount}: ${cc.get_fee(amount):.2f}")
    #
    # paypal = PayPalPayment("user@email.com")
    # print(f"PayPal fee on ${amount}: ${paypal.get_fee(amount):.2f}")
    #
    # crypto = CryptoPayment("0x1234...")
    # print(f"Crypto fee on ${amount}: ${crypto.get_fee(amount):.2f}")

    # # Test 5: Observer Pattern
    # print("\n--- Test 5: Observer Pattern (Notifications) ---")
    # order = Order("ORD-001", "Alice")
    # order.attach(EmailNotifier())
    # order.attach(SMSNotifier())
    # order.attach(InventoryManager())
    #
    # print("Changing order status:")
    # order.status = "CONFIRMED"
    # order.status = "SHIPPED"
    # order.status = "DELIVERED"

    # # Test 6: Full Integration
    # print("\n--- Test 6: Full Integration ---")
    # processor = OrderProcessor()
    #
    # # Create order
    # order = processor.create_order("ORD-002", "Bob")
    #
    # # Add products
    # processor.add_product_to_order(order, "electronics", "Phone", 699, warranty_years=1)
    # processor.add_product_to_order(order, "clothing", "Case", 29, size="Standard", material="Leather")
    #
    # print(f"Order total: ${order.get_total():.2f}")
    #
    # # Process payment
    # payment = CreditCardPayment("4111111111111111", "123", "12/25")
    # success, final = processor.process_payment(order, payment)
    # print(f"Payment {'successful' if success else 'failed'}: ${final:.2f}")

    print("\n" + "=" * 60)
    print("Implement the patterns and uncomment tests!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
