class Book:
    """Represents a book in the library."""
    def __init__(self, title, author):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Checks out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Returns the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """Returns a string representation of the book."""
        status = "Checked Out" if self._is_checked_out else "Available"
        return f'"{self.title}" by {self.author} ({status})'


class Library:
    """Manages the collection of books in the library."""
    def __init__(self):
        """Initializes a Library object with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)
        print(f'Added "{book.title}" to the library.')

    def check_out_book(self, title):
        """
        Checks out a book by its title.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f'"{book.title}" has been checked out.')
                    return
                else:
                    print(f'"{book.title}" is already checked out.')
                    return
        print(f'"{title}" not found in the library.')

    def return_book(self, title):
        """
        Returns a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f'"{book.title}" has been returned.')
                    return
                else:
                    print(f'"{book.title}" was not checked out.')
                    return
        print(f'"{title}" not found in the library.')

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            print("\n--- Available Books ---")
            for book in available_books:
                print(book)
            print("-----------------------")
