import math


class Automobile:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, distance):
        self.x += distance * math.cos(math.radians(self.angle))
        self.y += distance * math.sin(math.radians(self.angle))

    def turn(self, new_angle):
        self.angle = new_angle


class Bus(Automobile):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.passengers = 0
        self.money = 0

    def enter(self, num_passengers):
        self.passengers += num_passengers

    def exit(self, num_passengers):
        self.passengers = max(0, self.passengers - num_passengers)

    def move(self, distance):
        super().move(distance)
        self.money += distance * self.passengers * 0.5


car = Automobile(0, 0, 0)
car.move(10)
car.turn(90)
car.move(20)

bus = Bus(0, 0, 0)
bus.enter(5)
bus.move(10)
bus.exit(2)
bus.move(20)

print(f"Автомобиль: x={car.x:.2f}, y={car.y:.2f}, angle={car.angle:.2f}")
print(
    f"Автобус: x={bus.x:.2f}, y={bus.y:.2f}, angle={bus.angle:.2f}, passengers={bus.passengers}, money={bus.money:.2f}")
