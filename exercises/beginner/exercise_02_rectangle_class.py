"""
Exercise 2: Rectangle Class

Create a `Rectangle` class with:
- Attributes: width, height
- Methods:
  - area() - return width * height
  - perimeter() - return 2 * (width + height)
  - is_square() - return True if width == height
  - scale(factor) - multiply both dimensions by factor
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def is_square(self):
        return self.width == self.height
    def scale(self, factor):
      self.width *= factor
      self.height *= factor
# TODO: Write your Rectangle class here


# Test code (uncomment when ready)
rect = Rectangle(5, 10)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Is square? {rect.is_square()}")
rect.scale(2)
print(f"New area: {rect.area()}")
