"""
Create a class Library that stores a list of books
(each book is a dict with title and author).
Add methods add_book(), remove_book(), and list_books().
"""


class Library:

    def __init__(self) -> None:
        self.books = []

    def add_book(self, title: str, author: str) -> None:
        book = {"title": title, "author": author}
        self.books.append(book)
        print(f"Added: '{title}' by {author}")

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"Removed: {title}")
                return
        print(f"'{title}' not found in librabry")

    def list_book(self):
        if not self.books:
            print("No book in the library.")
            return
        for book in self.books:
            print(f"{book['title']} by {book['author']}")


library = Library()

library.add_book("The Hobbit", "J.R.R. Tolkien")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

library.list_book()

library.remove_book("The Hobbit")
print()
library.list_book()
