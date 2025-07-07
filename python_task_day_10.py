import random

# Base Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} - ${self.price} x {self.quantity} = ${self.total_value():.2f}"

# Subclass with expiry:
class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        total = super().total_value()
        return total * 0.8 if self.expiry_days < 5 else total

    def __str__(self):
        return f"{super().__str__()} (Expires in {self.expiry_days} days)"

# Inventory manager class:
class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def list_inventory(self):
        for i, p in enumerate(self.inventory, 1):
            print(f"{i}. {p}")

    def search_by_name(self, term):
        results = list(filter(lambda p: term.lower() in p.name.lower(), self.inventory))
        print("\nSearch Results:")
        for i, p in enumerate(results, 1):
            print(f"{i}. {p}")

    def restock_all(self):
        for product in self.inventory:
            product.quantity += random.randint(1, 10)


if __name__ == "__main__":
    manager = InventoryManager()

    # Adding products:
    manager.add_product(Product("Shampoo", 200, 5))
    manager.add_product(PerishableProduct("Milk", 100, 3, 2))
    manager.add_product(PerishableProduct("Yogurt", 80, 2, 7))
    manager.add_product(Product("Soap", 50, 10))

    print("📦 Inventory List:")
    manager.list_inventory()

    print("\n🔍 Search for 'milk':")
    manager.search_by_name("milk")

    print("\n📈 Restocking...")
    manager.restock_all()

    print("\n📦 Updated Inventory:")
    manager.list_inventory()
