""" Multiple Inheritance Instruction:

Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run()"""

class Bird:
    def fly(self):
        return "Bird is flying"

class Mammal:
    def run(self):
        return "Mammal is running"

class Bat(Bird, Mammal):
    def fly(self):
        return "Bat is flying"

    def run(self):
        return "Bat is running"

# Example usage:
bat = Bat()
print(bat.fly())  # Output: Bat is flying
print(bat.run())  # Output: Bat is running
