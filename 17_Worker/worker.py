class Worker:
    def __init__(self, name, position, experience):
        self.name = name
        self.position = position
        self.experience = experience

    def print_info(self):
        if self.experience % 10 in [2, 3, 4] and self.experience % 100 not in [12, 13, 14]:
            years_str = "года"
        elif self.experience % 10 == 1 and self.experience % 100 != 11:
            years_str = "год"
        else:
            years_str = "лет"

        print(f"Имя: {self.name} Должность: {self.position} Стаж: {self.experience} {years_str}")


worker1 = Worker("Алексей", "Программист", 17)
worker1.print_info()
print()

worker2 = Worker("Анна", "Маркетолог", 2)
worker2.print_info()
print()

worker3 = Worker("Дмитрий", "Аналитик", 1)
worker3.print_info()
print()
