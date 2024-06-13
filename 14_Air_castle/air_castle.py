class AirCastle:
    def __init__(self, height, num_clouds, color):
        self.height = height
        self.num_clouds = num_clouds
        self.color = color

    def change_height(self, value):
        self.height = max(self.height + value, 0)

    def __add__(self, n):
        self.num_clouds += n
        self.height += n // 5
        return self

    def __call__(self, transparency):
        visibility = self.height // transparency * self.num_clouds
        return visibility

    def __str__(self):
        return f"The AirCastle at an altitude of {self.height} meters is {self.color} with {self.num_clouds} clouds."

    def __gt__(self, other):
        if self.num_clouds != other.num_clouds:
            return self.num_clouds > other.num_clouds
        elif self.height != other.height:
            return self.height > other.height
        else:
            return self.color > other.color

    def __lt__(self, other):
        if self.num_clouds != other.num_clouds:
            return self.num_clouds < other.num_clouds
        elif self.height != other.height:
            return self.height < other.height
        else:
            return self.color < other.color

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return (
                self.height == other.height
                and self.num_clouds == other.num_clouds
                and self.color == other.color
        )

    def __ne__(self, other):
        return not self == other


castle1 = AirCastle(100, 10, "white")
castle2 = AirCastle(80, 8, "blue")

print(castle1)
print(castle2)

print(castle1 < castle2)
print(castle1 > castle2)

castle1.change_height(-20)
print(castle1)

castle1 + 5
print(castle1)

visibility = castle1(5)
print(visibility)
