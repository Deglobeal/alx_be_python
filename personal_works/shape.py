"""Single Inheritance Instruction:

Create a base class Shape with a method calculate_area().
Create a subclass Rectangle that inherits from Shape and overrides calculate_area() to calculate the area of a rectangle."""

class Shape:
    def calculate_area(self):
        """Base method to calculate area."""
        raise NotImplementedError("This method should be overridden in subclasses")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Override the base method to calculate the area of a rectangle."""
        return self.width * self.height

# Example usage:
# Creating an instance of Rectangle
rect = Rectangle(10, 5)
print(f"The area of the rectangle is: {rect.calculate_area()}")  # Output: The area of the rectangle is: 50
