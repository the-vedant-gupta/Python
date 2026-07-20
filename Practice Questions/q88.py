"""
Numbers to Cube
Using dictionary comprehension, create a new dictionary where keys are numbers from 1 to 10,
and values are the cube of each number
"""

cubes = {k: k**3 for k in range(0, 11)}
print(cubes)
