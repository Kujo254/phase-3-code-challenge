# lib/challenge.py

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """Associate a book with this author."""
        if book not in self.books:
            self.books.append(book)
            book.author = self  # set the book's author reference


class Book:
    def __init__(self, title, author=None, publisher=None):
        self.title = title
        self.author = None
        self.publisher = None

        if author:
            author.add_book(self)   # link to author if passed
        if publisher:
            publisher.publish_book(self)  # link to publisher if passed


class Publisher:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish_book(self, book):
        """Associate a book with this publisher."""
        if book not in self.books:
            self.books.append(book)
            book.publisher = self  # set the book's publisher reference
