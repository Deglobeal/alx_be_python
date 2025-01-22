class Person:
    def __init__(self, name, age):
        """
        Constructor to initialize the Person object with name and age.

        :param name: str, the name of the person
        :param age: int, the age of the person
        """
        self.name = name
        self.age = age
        print(f"Person object created for {self.name}, age {self.age}.")

    def __del__(self):
        """
        Destructor to clean up the Person object. Prints a farewell message.
        """
        print(f"Person object for {self.name} is being deleted. Farewell!")

# Example usage
if __name__ == "__main__":
    person = Person("Alice", 30)
    del person