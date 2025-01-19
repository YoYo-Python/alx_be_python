class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only instances of the Book class can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"You have checked out '{title}' by {book.author}."
        return f"The book '{title}' is not available."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"You have returned '{title}'."
        return f"The book '{title}' was not checked out."

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            return "\n".join([f"{book.title} by {book.author}" for book in available_books])
        return "No books are currently available."
