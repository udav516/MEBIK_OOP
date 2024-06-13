class Client:
    def __init__(self, code, name, open_date, deposit, percent):
        self.__code = code
        self.__name = name
        self.__open_date = open_date
        self.__deposit = deposit
        self.__percent = percent

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_open_date(self):
        return self.__open_date

    def get_deposit(self):
        return self.__deposit

    def get_percent(self):
        return self.__percent

    def __str__(self):
        return f"Код: {self.__code}, ФИО: {self.__name}, Дата открытия: {self.__open_date}, Размер вклада: {self.__deposit} руб., Процент: {self.__percent}%"


class Bank:
    def __init__(self):
        self.__client_base = []

    def add_client(self, client):
        self.__client_base.append(client)

    def show_by_money(self, money):
        for client in self.__client_base:
            if client.get_deposit() > money:
                print(client)

    def show_by_code(self, code):
        for client in self.__client_base:
            if client.get_code() == code:
                print(client)

    def show_by_proc(self, proc):
        for client in self.__client_base:
            if client.get_percent() > proc:
                print(client)

    def __str__(self):
        output = ""
        for client in self.__client_base:
            output += str(client) + "\n"
        return output


# Создаем несколько клиентов
client1 = Client(1001, "Иванов Иван Иванович", "01.01.2022", 100000, 5)
client2 = Client(1002, "Петров Петр Петрович", "15.03.2021", 50000, 3)
client3 = Client(1003, "Сидоров Сидор Сидорович", "01.09.2020", 200000, 7)

# Создаем банк и добавляем клиентов
bank = Bank()
bank.add_client(client1)
bank.add_client(client2)
bank.add_client(client3)

print("Информация о всех клиентах:")
print(bank)

print("Клиенты с вкладом больше 100000 рублей:")
bank.show_by_money(100000)
print()

print("Информация о клиенте с кодом 1002:")
bank.show_by_code(1002)
print()

print("Клиенты с процентом по вкладу больше 5%:")
bank.show_by_proc(5)
