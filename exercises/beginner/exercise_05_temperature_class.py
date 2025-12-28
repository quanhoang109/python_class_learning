"""
Exercise 5: Temperature Class

Create a `Temperature` class with:
- Instance attribute: celsius
- Instance methods:
  - to_fahrenheit() - return (celsius * 9/5) + 32
  - to_kelvin() - return celsius + 273.15
- Class methods:
  - from_fahrenheit(f) - create Temperature from Fahrenheit
  - from_kelvin(k) - create Temperature from Kelvin
- Static method:
  - is_freezing(celsius) - return True if <= 0
"""

# TODO: Write your Temperature class here
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    def to_kelvin(self):
        return self.celsius + 273.15
    @classmethod
    def from_fahrenheit(cls, f):
        celsius = (f - 32) * 5/9
        return cls(celsius)
    @classmethod
    def from_kelvin(cls, k):
        celsius = k - 273.15
        return cls(celsius)
    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0
# Test code (uncomment when ready)
temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.to_fahrenheit()}")
print(f"Kelvin: {temp.to_kelvin()}")
temp2 = Temperature.from_fahrenheit(77)
print(f"77°F = {temp2.celsius}°C")

print(f"Is freezing? {Temperature.is_freezing(-5)}")
