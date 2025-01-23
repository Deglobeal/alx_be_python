# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __str__(self):
        return self.get_details()

class EBook(Book):
    def __init__(self, title, author, file_size):
        # Initialize base class
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, File Size: {self.file_size}MB"

    def __str__(self):
        return self.get_details()

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Initialize base class
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Page Count: {self.page_count}"

    def __str__(self):
        return self.get_details()

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)  # Now, `book` will automatically call `__str__` when printed.
