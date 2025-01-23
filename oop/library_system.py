# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to display a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example of usage
if __name__ == "__main__":
    # Creating a Book instance
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    
    # Print the string representation of the book
    print(book1)
    
    # Print the official representation of the book
    print(repr(book1))

    # Deleting the book instance (to trigger the __del__ method)
    del book1
