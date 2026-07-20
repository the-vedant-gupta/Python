"""
World Capitals
Create a dictionary mapping fice countries and capital cities. Iterate through this dictionary teh items() method and'
print each pair in the format: Countary --> Capital
"""

countries = {
    "India": "New Delhi",
    "France": "Paris",
    "Australia": "Melbourn",
    "U.K.": "London",
    "U.S.A": "Washington DC",
}

for country, capital in countries.items():
    print(f"{country} --> {capital}")
