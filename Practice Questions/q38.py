"""
Write a function called rectangle_area that takes length and breadth
as parameters and prints the area.
"""


def rectangle(length, breadth):
    area = length * breadth
    parameter = 2 * (length + breadth)
    print(f"Area of rectangle is {area} and parameter is {parameter}")


rectangle(4, 5)
