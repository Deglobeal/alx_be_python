# Base class
class Animal:
    def eat(self):
        return "This animal is eating."
    
    def sleep(self):
        return "This animal is sleeping."

# Subclass
class Dog(Animal):
    def bark(self):
        return "Woof! Woof!"

# Creating instances
animal = Animal()
dog = Dog()

# Demonstrating method inheritance and added behavior
print(animal.eat())  # Output: This animal is eating.
print(animal.sleep())  # Output: This animal is sleeping.

print(dog.eat())  # Output: This animal is eating. (inherited from Animal)
print(dog.sleep())  # Output: This animal is sleeping. (inherited from Animal)
print(dog.bark())  # Output: Woof! Woof! (specific to Dog)
