# lib/challenge.py

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """Associate a book with this author."""
        if book not in self.books:
            self.books.append(book)
            book.author = self

    def book_count(self):
        """Return how many books this author has written."""
        return len(self.books)


class Book:
    def __init__(self, title, author=None, publisher=None):
        self.title = title
        self.author = None
        self.publisher = None

        if author:
            author.add_book(self)
        if publisher:
            publisher.publish_book(self)


class Publisher:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish_book(self, book):
        """Associate a book with this publisher."""
        if book not in self.books:
            self.books.append(book)
            book.publisher = self

    def book_count(self):
        """Return how many books this publisher has published."""
        return len(self.books)

    def authors(self):
        """Return a set of unique authors who published with this publisher."""
        return {book.author for book in self.books if book.author}
