class Book:
    def __init__(self, title, author, pages):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            pages (int): The number of pages in the book.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        Return a user-friendly string representation of the book.

        Returns:
            str: A readable description of the book.
        """
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def __repr__(self):
        """
        Return an unambiguous string representation of the book.

        Returns:
            str: A string that could be used to recreate the book object.
        """
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

# Example usage
book = Book("1984", "George Orwell", 328)
print(str(book))  # Output: '1984' by George Orwell, 328 pages
print(repr(book)) # Output: Book(title='1984', author='George Orwell', pages=328)"
