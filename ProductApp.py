class Product:
    def __init__(self, pid, name, category, price):
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price

class ProductApp:
    def __init__(self):
        self.products = []

    # 1. Add Product
    def add_product(self, pid, name, category, price):
        new_product = Product(pid, name, category, price)
        self.products.append(new_product)
        print(f"Product '{name}' added successfully.")

    # 2. Update Product
    def update_product(self, pid, name=None, category=None, price=None):
        for product in self.products:
            if product.pid == pid:
                if name: product.name = name
                if category: product.category = category
                if price: product.price = price
                print(f"Product with ID {pid} updated successfully.")
                return
        print(f"Product with ID {pid} not found.")

    # 3. Delete Product
    def delete_product(self, pid):
        for product in self.products:
            if product.pid == pid:
                self.products.remove(product)
                print(f"Product with ID {pid} deleted successfully.")
                return
        print(f"Product with ID {pid} not found.")

    # 4. Get Product By PId
    def get_product_by_pid(self, pid):
        for product in self.products:
            if product.pid == pid:
                return vars(product)
        return f"Product with ID {pid} not found."

    # 5. Get All Products
    def get_all_products(self):
        return [vars(product) for product in self.products]

    # 6. Get Products By Category
    def get_products_by_category(self, category):
        return [vars(product) for product in self.products if product.category == category]

    # 7. Get Products Between Prices
    def get_products_between_prices(self, min_price, max_price):
        return [vars(product) for product in self.products if min_price <= product.price <= max_price]




app = ProductApp()

# Adding products
app.add_product(1, "Laptop", "Electronics", 1000)
app.add_product(2, "Phone", "Electronics", 500)
app.add_product(3, "Shirt", "Clothing", 50)

# Updating a product
app.update_product(1, price=950)

# Deleting a product
app.delete_product(3)

# Getting product by PId
print(app.get_product_by_pid(1))

# Getting all products
print(app.get_all_products())

# Getting products by category
print(app.get_products_by_category("Electronics"))

# Getting products between prices
print(app.get_products_between_prices(100, 1000))