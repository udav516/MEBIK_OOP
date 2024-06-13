class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        if self._plant.tomatoes:
            self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"Садовник {self.name} собрал урожай!")
        else:
            print(f"Садовник {self.name} пока не может собирать урожай, не все томаты созрели.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("- Для ухода за томатами необходимо регулярно поливать куст и удалять сорняки.")
        print("- Томаты готовы к сбору урожая, когда они полностью краснеют.")
        print("- Собирайте томаты аккуратно, не повреждая куст.")


class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            return True
        return False


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


Gardener.knowledge_base()

bush = TomatoBush(10)
gardener = Gardener("Иван", bush)

for _ in range(3):
    gardener.work()

gardener.harvest()

while not bush.all_are_ripe():
    gardener.work()
    gardener.harvest()

gardener.harvest()
