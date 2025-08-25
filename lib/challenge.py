# lib/challenge.py

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []  # will hold books written by this author


class Book:
    def __init__(self, title, author=None, publisher=None):
        self.title = title
        self.author = author
        self.publisher = publisher


class Publisher:
    def __init__(self, name):
        self.name = name
        self.books = []  # will hold books published by this publisher
