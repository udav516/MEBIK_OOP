class Snow:
    def __init__(self, count):
        self.count = count

    def __add__(self, n):
        return Snow(self.count + n)

    def __sub__(self, n):
        return Snow(self.count - n)

    def __mul__(self, n):
        return Snow(self.count * n)

    def __truediv__(self, n):
        return Snow(self.count // n)

    def make_snow(self, row_count):
        snow_row = "*" + "_" * (row_count - 2) + "*"
        snow_pattern = "\n".join([snow_row] * row_count)
        return snow_pattern


snow = Snow(100)

snow_more = snow + 50
print(snow_more.count)

snow_less = snow / 2
print(snow_less.count)

snow_pattern = snow_more.make_snow(5)
print(snow_pattern)
