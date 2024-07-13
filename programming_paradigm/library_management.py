class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available

    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False
            
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.checkout():
                    print(f"Checked out: {book.title}")
                else:
                    print(f"{book.title} is already checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book.title}")
                else:
                    print(f"{book.title} is already available.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for title in available_books:
                print(f"{title}")
        else:
            print("No books available.")
