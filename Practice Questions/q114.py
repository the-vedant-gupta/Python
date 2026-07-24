"""
Create a class Movie with attributes title, director, year, rating.
Add a method is_classic() that returns True if the movie is more than 25 years old.
"""

from datetime import datetime


class Movie:

    def __init__(self, title: str, director: str, year: int, rating: float) -> None:
        self.title: str = title
        self.director: str = director
        self.year: int = year
        self.rating: float = rating

    def is_classic(self):
        print(
            f"Movie Name= {self.title}, Director: {self.director}, Year: {self.year} and rating: {self.rating} "
        )
        current_year = datetime.now().year
        return f"Is Classic: {(current_year - self.year) > 25} "


m1 = Movie("fdd", "dddd0", 2012, 7.7)
print(m1.is_classic())
