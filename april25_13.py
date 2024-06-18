class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def remove_product(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"{product_name} removed from cart.")
                return
        print(f"{product_name} is not in the cart.")

    def view_cart(self):
        print("Shopping Cart:")
        total_price = 0
        for item in self.items:
            print(f"Name: {item.name}, Price: ${item.price}, Quantity: {item.quantity}")
            total_price += item.price
        print(f"Total Price: ${total_price}")


# Example usage:

# Create customers
customer1 = Customer("Alice", "alice@example.com", "123 Main St, City")
customer2 = Customer("Bob", "bob@example.com", "456 Oak St, Town")

# Create products
product1 = Product("Laptop", 1000, 1)
product2 = Product("Headphones", 50, 2)
product3 = Product("Keyboard", 80, 1)

# Create shopping carts
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Customer 1 adds products to their cart
cart1.add_product(product1)
cart1.add_product(product2)

# Customer 2 adds products to their cart
cart2.add_product(product2)
cart2.add_product(product3)

# Customer 1 removes a product from their cart
cart1.remove_product("Laptop")

# Customer 1 views their cart
cart1.view_cart()

# Customer 2 views their cart
cart2.view_cart()
