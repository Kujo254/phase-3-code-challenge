# tests/test_challenge.py

import unittest
from lib.challenge import Author, Book, Publisher


class TestChallenge(unittest.TestCase):

    def test_author_adds_books(self):
        author = Author("George Orwell")
        book1 = Book("1984")
        book2 = Book("Animal Farm")

        author.add_book(book1)
        author.add_book(book2)

        self.assertEqual(author.book_count(), 2)
        self.assertIn(book1, author.books)
        self.assertIn(book2, author.books)
        self.assertEqual(book1.author, author)

    def test_publisher_publishes_books(self):
        publisher = Publisher("Penguin")
        book = Book("Brave New World")

        publisher.publish_book(book)

        self.assertEqual(publisher.book_count(), 1)
        self.assertIn(book, publisher.books)
        self.assertEqual(book.publisher, publisher)

    def test_publisher_authors(self):
        author1 = Author("Author A")
        author2 = Author("Author B")
        publisher = Publisher("HarperCollins")

        book1 = Book("Book One", author=author1, publisher=publisher)
        book2 = Book("Book Two", author=author2, publisher=publisher)
        book3 = Book("Book Three", author=author1, publisher=publisher)

        authors = publisher.authors()

        self.assertEqual(len(authors), 2)
        self.assertIn(author1, authors)
        self.assertIn(author2, authors)


if __name__ == "__main__":
    unittest.main()
