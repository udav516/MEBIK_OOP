class Bus:
    def __init__(self, speed, capacity, max_speed):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.has_empty_seats = True
        self.seats = {i: None for i in range(1, capacity + 1)}

    def board(self, *passengers):
        for passenger in passengers:
            if len(self.passengers) < self.capacity:
                self.passengers.append(passenger)
                for seat, name in self.seats.items():
                    if name is None:
                        self.seats[seat] = passenger
                        break
                print(f"{passenger} сел в автобус.")
            else:
                print("Автобус переполнен.")
        self.has_empty_seats = len(self.passengers) < self.capacity

    def alight(self, *passengers):
        for passenger in passengers:
            if passenger in self.passengers:
                self.passengers.remove(passenger)
                for seat, name in self.seats.items():
                    if name == passenger:
                        self.seats[seat] = None
                        break
                print(f"{passenger} вышел из автобуса.")
        self.has_empty_seats = len(self.passengers) < self.capacity

    def increase_speed(self, speed_increase):
        self.speed = min(self.speed + speed_increase, self.max_speed)
        print(f"Скорость автобуса увеличилась до {self.speed} км/ч.")

    def decrease_speed(self, speed_decrease):
        self.speed = max(self.speed - speed_decrease, 0)
        print(f"Скорость автобуса снизилась до {self.speed} км/ч.")

    def __contains__(self, passenger):
        return passenger in self.passengers

    def __iadd__(self, passenger):
        self.board(passenger)
        return self

    def __isub__(self, passenger):
        self.alight(passenger)
        return self


bus = Bus(speed=50, capacity=40, max_speed=80)
bus.board("Alice", "Bob", "Charlie", "David")
print(bus.seats)
print(bus.passengers)
print(bus.has_empty_seats)

bus -= "Bob"
bus -= "Charlie"
print(bus.seats)
print(bus.passengers)
print(bus.has_empty_seats)

print("Alice" in bus)
print("Bob" in bus)

bus.increase_speed(10)
bus.decrease_speed(20)
