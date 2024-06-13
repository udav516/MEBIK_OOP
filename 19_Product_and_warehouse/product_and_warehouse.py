class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price

    def __add__(self, other):
        return Product(self.__name, self.__store, self.__price + other.__price)

    def __str__(self):
        return f"{self.__name} ({self.__store}) - {self.__price} руб."


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_product_by_index(self, index):
        return self.__products[index]

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                return product
        return None

    def sort_by_store(self):
        self.__products.sort(key=lambda x: x.get_store())

    def sort_by_name(self):
        self.__products.sort(key=lambda x: x.get_name())

    def sort_by_price(self):
        self.__products.sort(key=lambda x: x.get_price())

    def __add__(self, other):
        result = Warehouse()
        for product in self.__products:
            result.add_product(product)
        for product in other.__products:
            result.add_product(product)
        return result

    def __str__(self):
        output = ""
        for product in self.__products:
            output += str(product) + "\n"
        return output


product1 = Product("Яблоки", "Магазин 1", 50)
product2 = Product("Молоко", "Магазин 2", 80)
product3 = Product("Хлеб", "Магазин 1", 30)

warehouse = Warehouse()
warehouse.add_product(product1)
warehouse.add_product(product2)
warehouse.add_product(product3)
print(warehouse)
print(warehouse.get_product_by_index(1), '\n')

print(warehouse.get_product_by_name("Хлеб"), '\n')

warehouse.sort_by_store()
print("Сортировка по названию магазина:")
print(warehouse)

warehouse.sort_by_name()
print("Сортировка по наименованию:")
print(warehouse)

warehouse.sort_by_price()
print("Сортировка по цене:")
print(warehouse)

new_warehouse = warehouse + warehouse
print("Сложение двух складов:")
print(new_warehouse)
