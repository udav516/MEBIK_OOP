class Human:
    default_name = "John Doe"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Деньги: {self.__money}")
        print(f"Дом: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Имя по умолчанию: {Human.default_name}")
        print(f"Возраст по умолчанию: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount=0):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            print(f"{self.name} купил дом!")
        else:
            print(f"У {self.name} недостаточно денег, чтобы купить дом.")


class House:
    def __init__(self, area, price):
        self.__area = area
        self.__price = price

    def final_price(self, discount):
        return self.__price * (1 - discount)


class SmallHouse(House):
    def __init__(self):
        super().__init__(area=40, price=100000)


Human.default_info()
person = Human()
person.info()
small_house = SmallHouse()
person.buy_house(small_house)
person.earn_money(150000)
person.buy_house(small_house, 0.1)
person.info()
