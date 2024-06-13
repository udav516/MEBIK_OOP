class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def fly(self):
        return self.bee_part >= self.elephant_part

    def trumpet(self):
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo!"
        else:
            return "wzzzzz"

    def eat(self, meal, value):
        if meal == 'nectar':
            self.elephant_part = max(0, self.elephant_part - value)
            self.bee_part = min(100, self.bee_part + value)
        elif meal == 'grass':
            self.bee_part = max(0, self.bee_part - value)
            self.elephant_part = min(100, self.elephant_part + value)

    def get_parts(self):
        return [self.bee_part, self.elephant_part]


# Пример 1
be = BeeElephant(3, 2)
print(be.fly())  # True
print(be.trumpet())  # wzzzzz
be.eat('grass', 4)
print(be.get_parts())  # (0, 6)

# Пример 2
be = BeeElephant(13, 87)
print(be.fly())  # False
print(be.trumpet())  # tu-tu-doo-doo!
be.eat('nectar', 90)
print(be.trumpet())  # wzzzzz
print(be.get_parts())  # (100, 0)
