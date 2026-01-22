"""
Exercise 13: Vehicle Rental System (SOLID Principles)

Create a vehicle rental system applying SOLID principles:

┌─────────────────────────────────────────────────────────────────────┐
│ SOLID PRINCIPLES TO APPLY                                           │
├─────────────────────────────────────────────────────────────────────┤
│ S - Single Responsibility: Separate classes for different concerns │
│ O - Open/Closed: Use abstract base class for vehicles              │
│ L - Liskov Substitution: All vehicles work with rental system      │
│ I - Interface Segregation: Small focused interfaces                │
│ D - Dependency Inversion: Depend on abstractions                   │
└─────────────────────────────────────────────────────────────────────┘

Classes to implement:

1. Abstract Base Class:
   - Vehicle (ABC) - brand, model, year, daily_rate, is_available
     Methods: get_info(), calculate_rental_cost(days)

2. Concrete Vehicle Classes (extend Vehicle):
   - Car - seats, fuel_type
   - Motorcycle - engine_size
   - Truck - cargo_capacity

3. Support Classes:
   - Customer - name, customer_id, rental_history (list)
   - Rental - vehicle, customer, start_date, days, total_cost

4. Service Classes (Single Responsibility):
   - VehicleRepository - manage vehicle storage (add, remove, find)
   - CustomerRepository - manage customer storage
   - RentalService - handle rental logic (rent, return, calculate)
   - NotificationService (optional) - send rental confirmations

5. Main Class:
   - RentalAgency - coordinates all services

Features:
- Add/remove vehicles and customers
- Rent vehicle (check availability)
- Return vehicle and calculate final cost
- Search vehicles by type, price range
- Get customer rental history
- Display all available vehicles

BONUS CHALLENGES:
- Add discount strategies (percentage, fixed, loyalty)
- Add insurance options using composition
- Implement Observer pattern for notifications
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta


# =============================================================================
# TODO: Implement your classes here following SOLID principles
# =============================================================================

# Example structure (implement the methods):

class Vehicle(ABC):
    """Abstract base class for all vehicles (Open/Closed Principle)."""

    def __init__(self, brand, model, year, daily_rate):
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.is_available = True

    @abstractmethod
    def get_vehicle_type(self):
        """Return the type of vehicle."""
        pass

    def get_info(self):
        """Get vehicle information."""
        return f"{self.year} {self.brand} {self.model} - ${self.daily_rate}/day"

    def calculate_rental_cost(self, days):
        """Calculate rental cost for given days."""
        return self.daily_rate * days


class Car(Vehicle):
    """Car class extending Vehicle."""

    def __init__(self, brand, model, year, daily_rate, seats, fuel_type):
        super().__init__(brand, model, year, daily_rate)
        self.seats = seats
        self.fuel_type = fuel_type

    def get_vehicle_type(self):
        return "Car"
    


class Motorcycle(Vehicle):
    """Motorcycle class extending Vehicle."""
    # TODO: Implement
    def __init__(self, brand, model, year, daily_rate, engine_size):
        super().__init__(brand, model, year, daily_rate)
        self.engine_size = engine_size
    pass
    def get_vehicle_type(self):
        return "Mortorcycle"

class Truck(Vehicle):
    """Truck class extending Vehicle."""
    # TODO: Implement
    def __init__(self, brand, model, year, daily_rate, cargo_capacity):
        super().__init__(brand, model, year, daily_rate)
        self.cargo_capacity = cargo_capacity
    pass
    def get_vehicle_type(self):
            return "Truck"


class Customer:
    """Customer class."""
    # TODO: Implement
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rental_history = []
    pass


class Rental:
    """Represents a single rental transaction."""
    # TODO: Implement
    def __init__(self, vehicle, customer, start_date, days):
        self.vehicle = vehicle
        self.customer = customer
        self.start_date = start_date
        self.days = days
        self.total_cost = vehicle.calculate_rental_cost(days)
    pass


class VehicleRepository:
    """Manages vehicle storage (Single Responsibility)."""
    # TODO: Implement
    def __init__(self):
        self.vehicles = []
    pass
    def add(self,vehicle):
        self.vehicles.append(vehicle)
    def remove(self,vehicle):
        self.vehicles.remove(vehicle)
    def find(self,criteria):
        # Implement search logic based on criteria
        pass
    def get_available(self):
        return [v for v in self.vehicles if v.is_available]


class CustomerRepository:
    """Manages customer storage (Single Responsibility)."""
    # TODO: Implement
    def __init__(self):
        self.customers = []
    def add(self,customer):
        self.customers.append(customer)
    def remove(self,customer):
        self.customers.remove(customer)
    def find(self,customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None 
    pass


class RentalService:
    """Handles rental logic (Single Responsibility)."""
    # TODO: Implement
    def __init__(self):
        self.rentals = []
    def rent_vehicle(self, customer, vehicle, days):
        if vehicle.is_available:
            rental=  Rental(vehicle, customer, datetime.now(), days)
            vehicle.is_available = False
            customer.rental_history.append(rental)
            self.rentals.append(rental)
            return rental
        else:
            raise Exception("Vehicle not available")
    def return_vehicle(self, rental):
        rental.vehicle.is_available = True
        return rental.total_cost
    pass


class RentalAgency:
    """Main class that coordinates services (Dependency Inversion)."""

    def __init__(self, name, vehicle_repo=None, customer_repo=None, rental_service=None):
        self.name = name
        # Depend on abstractions/interfaces, not concrete implementations
        self.vehicle_repo = vehicle_repo or VehicleRepository()
        self.customer_repo = customer_repo or CustomerRepository()
        self.rental_service = rental_service or RentalService()

    # TODO: Implement coordination methods
    def add_vehicle(self, vehicle):
        self.vehicle_repo.add(vehicle)  
    def add_customer(self, customer):
        self.customer_repo.add(customer)
    pass


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("=" * 60)
    print("VEHICLE RENTAL SYSTEM - TESTS")
    print("=" * 60)

    # TODO: Uncomment and run tests after implementing classes

    # Test 1: Create vehicles
    print("\n--- Test 1: Create Vehicles ---")
    car = Car("Toyota", "Camry", 2024, 50, seats=5, fuel_type="Gasoline")
    motorcycle = Motorcycle("Honda", "CBR600", 2023, 30, engine_size=600)
    truck = Truck("Ford", "F-150", 2022, 80, cargo_capacity=1000)
    
    print(f"Car: {car.get_info()}")
    print(f"Motorcycle: {motorcycle.get_info()}")
    print(f"Truck: {truck.get_info()}")
    
    # Test 2: Liskov Substitution - all vehicles work the same way
    print("\n--- Test 2: Liskov Substitution ---")
    vehicles = [car, motorcycle, truck]
    for vehicle in vehicles:
        print(f"{vehicle.get_vehicle_type()}: {vehicle.calculate_rental_cost(3)} for 3 days")
    
    # Test 3: Rental Agency with services
    print("\n--- Test 3: Rental Agency ---")
    agency = RentalAgency("Best Rentals")
    
    agency.vehicle_repo.add(car)
    agency.vehicle_repo.add(motorcycle)
    agency.vehicle_repo.add(truck)
    
    customer = Customer("Alice", "C001")
    agency.customer_repo.add(customer)
    
    # Test 4: Rent a vehicle
    print("\n--- Test 4: Rent Vehicle ---")
    rental = agency.rental_service.rent_vehicle(customer, car, days=3)
    print(f"Rental created: {rental}")
    
    # Test 5: Check availability
    print("\n--- Test 5: Available Vehicles ---")
    available = agency.vehicle_repo.get_available()
    print(f"Available vehicles: {len(available)}")
    
    # Test 6: Return vehicle
    print("\n--- Test 6: Return Vehicle ---")
    agency.rental_service.return_vehicle(rental)
    print(f"Vehicle returned. Cost: ${rental.total_cost}")

    print("\n" + "=" * 60)
    print("Implement the classes and uncomment tests!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
