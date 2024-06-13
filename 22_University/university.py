import datetime


class Persona:
    def __init__(self, surname, birth_date):
        self.surname = surname
        self.birth_date = birth_date

    def get_info(self):
        print(f"Фамилия: {self.surname}")
        print(f"Дата рождения: {self.birth_date}")

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (
                today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age


class Applicant(Persona):
    def __init__(self, surname, birth_date, faculty):
        super().__init__(surname, birth_date)
        self.faculty = faculty

    def get_info(self):
        super().get_info()
        print(f"Факультет: {self.faculty}")


class Student(Persona):
    def __init__(self, surname, birth_date, faculty, course):
        super().__init__(surname, birth_date)
        self.faculty = faculty
        self.course = course

    def get_info(self):
        super().get_info()
        print(f"Факультет: {self.faculty}")
        print(f"Курс: {self.course}")


class Professor(Persona):
    def __init__(self, surname, birth_date, faculty, position, experience):
        super().__init__(surname, birth_date)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def get_info(self):
        super().get_info()
        print(f"Факультет: {self.faculty}")
        print(f"Должность: {self.position}")
        print(f"Стаж: {self.experience} лет")


persons = [
    Applicant("Иванов", datetime.date(2000, 5, 15), "Физический"),
    Student("Петров", datetime.date(1999, 11, 20), "Математический", 3),
    Professor("Сидоров", datetime.date(1970, 3, 1), "Информационных технологий", "Профессор", 25)
]

for person in persons:
    person.get_info()
    print()

age_range = (20, 30)
for person in persons:
    if age_range[0] <= person.get_age() <= age_range[1]:
        person.get_info()
        print()
