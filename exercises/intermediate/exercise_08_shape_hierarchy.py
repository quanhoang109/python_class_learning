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


# TODO: Write total_area function here


# Test code (uncomment when ready)
# shapes = [
#     Circle(5),
#     Rectangle(4, 6),
#     Triangle(3, 4, 5)
# ]
#
# for shape in shapes:
#     print(f"{shape.__class__.__name__}: Area={shape.area():.2f}, Perimeter={shape.perimeter():.2f}")
#
# print(f"Total area: {total_area(shapes):.2f}")
