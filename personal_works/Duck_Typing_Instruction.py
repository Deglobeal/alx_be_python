"""Polymorphism with Duck Typing Instruction:

Create classes Dog, Cat, and Bird, each with a method make_sound().
Implement different behaviors for make_sound() in each class.
Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically."""

class Dog:
    def make_sound(self):
        return "Woof! Woof!"

class Cat:
    def make_sound(self):
        return "Meow! Meow!"

class Bird:
    def make_sound(self):
        return "Chirp! Chirp!"

def let_them_speak(animals):
    for animal in animals:
        print(animal.make_sound())

# Create instances of each class
dog = Dog()
cat = Cat()
bird = Bird()

# Create a list of animal objects
animals = [dog, cat, bird]

# Call the function to demonstrate polymorphism
let_them_speak(animals)
