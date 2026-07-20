"""
Product Price Lookup(HW)
Construct a dictionary containing four products names and their prices. Prompt the user to enter a product name.
Use the in keyword to check if it exists, if so, display its price. Otherwise inform teh user "Product not found"
"""

products = {
    "Laptop": 34,
    "Mobile": 54,
    "Earbuds": 45,
    "Mouse": 22,
    "Keyboard": 94,
}

product_name = input("Enter the Item: ")
if product_name in products:
    print(f"Price:", products[product_name])
else:
    print("Item Not found")
