# book_class.py

class Book:
    def __init__(self, title, author, year):
        # Constructor to initialize the book's title, author, and year
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' by {self.author} created!")

    def __del__(self):
        # Destructor that prints when a Book object is deleted
        print(f"Deleting '{self.title}'")

    def __str__(self):
        # String representation method for a user-friendly output
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official representation that can be used to recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example Usage (outside of the class)
if __name__ == "__main__":
    # Creating instances of Book
    book1 = Book("Pride and Prejudice", "Jane Austen", 1813)
    book2 = Book("1984", "George Orwell", 1949)

    # Using __str__ and __repr__
    print(book1)  # This calls __str__
    print(repr(book2))  # This calls __repr__

    # Deleting the objects to trigger __del__
    del book1
    del book2
