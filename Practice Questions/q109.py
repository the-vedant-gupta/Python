"""
Create a class Book with attributes title, author, and
pages. Create three book objects and print their details.
"""


class Book:

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

    def get_details(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages : {self.pages}")
        print("-" * 25)


b1 = Book("ABC", "Vedant", 33)
b1.get_details()
