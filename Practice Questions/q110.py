"""
Add a method describe() to the Book class that
prints: '<title>' by <author>, <pages> pages.
"""


class Book:

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

    def describe(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")


b1 = Book("ABC", "Vedant", 33)
b1.describe()
