import math

# Base Class - Shape
class Shape:
    def area(self):
        # This method is intended to be overridden by derived classes
        raise NotImplementedError("Subclasses must implement the 'area' method.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Override the area method to calculate area of rectangle
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Override the area method to calculate area of circle
        return math.pi * (self.radius ** 2)

# Demonstration of Polymorphism
if __name__ == "__main__":
    # Adjust dimensions to match expected output
    rectangle = Rectangle(10, 5)  # Length = 10, Width = 5 -> 10 * 5 = 50
    circle = Circle(7)            # Radius = 7 -> π * 7² = 153.93804002589985

    # Call the area method on both instances
    print(f"The area of the Rectangle is: {rectangle.area()}")
    print(f"The area of the Circle is: {circle.area()}")
