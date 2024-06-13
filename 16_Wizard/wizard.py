class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if self.rating + value > 100:
            self.rating = 100
        elif self.rating + value < 1:
            self.rating = 1
        else:
            self.rating += value
            if value > 0:
                self.age = max(18, self.age - abs(value) // 10)
            else:
                self.age = self.age - abs(value) // 10

    def __add__(self, string):
        self.change_rating(len(string))
        return self

    def __call__(self, arg):
        return (arg - self.age) * self.rating

    def __str__(self):
        return f"Wizard {self.name} with {self.rating} rating looks {self.age} years old"

    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        elif self.age != other.age:
            return self.age < other.age
        else:
            return self.name < other.name

    def __gt__(self, other):
        if self.rating != other.rating:
            return self.rating > other.rating
        elif self.age != other.age:
            return self.age > other.age
        else:
            return self.name > other.name

    def __le__(self, other):
        if self.rating != other.rating:
            return self.rating <= other.rating
        elif self.age != other.age:
            return self.age <= other.age
        else:
            return self.name <= other.name

    def __ge__(self, other):
        if self.rating != other.rating:
            return self.rating >= other.rating
        elif self.age != other.age:
            return self.age >= other.age
        else:
            return self.name >= other.name

    def __eq__(self, other):
        return self.rating == other.rating and self.age == other.age and self.name == other.name

    def __ne__(self, other):
        return self.rating != other.rating or self.age != other.age or self.name != other.name


wizard1 = Wizard("Merlin", 80, 75)
wizard2 = Wizard("Gandalf", 90, 60)
wizard3 = Wizard("Dumbledore", 85, 85)

print(wizard1)
print(wizard2)
print(wizard3)

wizard1.change_rating(10)
print(wizard1)

wizard2.change_rating(-15)
print(wizard2)

wizard3 += "Powerful"
print(wizard3)

result = wizard2(100)
print(result)

print(wizard1 > wizard2)
print(wizard2 <= wizard3)
print(wizard1 == wizard3)
