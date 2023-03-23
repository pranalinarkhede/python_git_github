from collections import namedtuple

# define a named tuple type called Product
Product = namedtuple('Product', ['name', 'price', 'category'])

# create a list of Product instances
products = [
    Product('Smartphone', 799.99, 'Electronics'),
    Product('Sneakers', 99.99, 'Apparel'),
    Product('Headphones', 149.99, 'Electronics'),
    Product('Backpack', 49.99, 'Accessories'),
    Product('SmartWatch', 125.99, 'Electronics'),
    Product('Mouse', 49.99, 'Electronics'),
    Product('Boots', 199.99, 'Apparel'),
    Product('Wallet', 29.99, 'Accessories')
]

# calculate the total price of all products in the Electronics category
total_price = sum(product.price for product in products if product.category == 'Apparel')
print(f"The total price of all apparel products is ${total_price:.2f}")