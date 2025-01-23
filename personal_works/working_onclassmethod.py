
class Book:
    # Class variable to count the number of book instances created
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment the count when a new book instance is created
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        # Class method to display the total number of books
        print(f"Total books created: {cls.total_books}")

# Create instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("Pride and Prejudice", "Jane Austen")

# Display the total number of books created
Book.display_total_books()
