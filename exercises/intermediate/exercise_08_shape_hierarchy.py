"""
Exercise 8: Shape Hierarchy

Create shape classes with inheritance:

Base class `Shape` (Abstract):
- Abstract methods: area(), perimeter()

Child classes:
- Circle(Shape) - attributes: radius
- Rectangle(Shape) - attributes: width, height
- Triangle(Shape) - attributes: side1, side2, side3

Each should implement area() and perimeter().

Create a function total_area(shapes) that calculates total area of a list of shapes.
"""

from abc import ABC, abstractmethod
import math

# TODO: Write your Shape, Circle, Rectangle, and Triangle classes here
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
# TODO: Write total_area function here
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super().__init__()
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape): 
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().__init__()
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5 # Heron's formula
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

# Test code (uncomment when ready)
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}: Area={shape.area():.2f}, Perimeter={shape.perimeter():.2f}")

print(f"Total area: {total_area(shapes):.2f}")
