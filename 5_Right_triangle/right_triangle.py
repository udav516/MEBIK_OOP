import math


class RightTriangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def increase_side(self, percent):
        self.a = self.a * (1 + percent / 100)
        self.b = self.b * (1 + percent / 100)

    def decrease_side(self, percent):
        self.a = self.a * (1 - percent / 100)
        self.b = self.b * (1 - percent / 100)

    def circumscribed_radius(self):
        return (self.a * self.b) / (2 * math.sqrt(self.a ** 2 + self.b ** 2))

    def perimeter(self):
        c = math.sqrt(self.a ** 2 + self.b ** 2)
        return self.a + self.b + c

    def angles(self):
        alpha = math.degrees(math.asin(self.a / math.sqrt(self.a ** 2 + self.b ** 2)))
        beta = math.degrees(math.asin(self.b / math.sqrt(self.a ** 2 + self.b ** 2)))
        gamma = 90.0
        return alpha, beta, gamma


triangle = RightTriangle(3, 4)
print(f"Исходные стороны треугольника: a = {triangle.a}, b = {triangle.b}")
triangle.increase_side(20)
print(f"Стороны треугольника после увеличения на 20%: a = {triangle.a:.2f}, b = {triangle.b:.2f}")
triangle.decrease_side(10)
print(f"Стороны треугольника после уменьшения на 10%: a = {triangle.a:.2f}, b = {triangle.b:.2f}")
radius = triangle.circumscribed_radius()
print(f"Радиус описанной окружности: {radius:.2f}")
perimeter = triangle.perimeter()
print(f"Периметр треугольника: {perimeter:.2f}")
alpha, beta, gamma = triangle.angles()
print(f"Углы треугольника: α = {alpha:.2f}°, β = {beta:.2f}°, γ = {gamma:.2f}°")
