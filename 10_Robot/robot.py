class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = [(x, y)]

    def move(self, commands):
        for command in commands:
            if command == 'N':
                self.y += 1
            elif command == 'S':
                self.y -= 1
            elif command == 'E':
                self.x += 1
            elif command == 'W':
                self.x -= 1
            self.x = max(0, min(100, self.x))
            self.y = max(0, min(100, self.y))
            self.path.append((self.x, self.y))
        return [(self.x, self.y)]

    def path(self):
        return self.path


robot = Robot(10, 20)

path = robot.move("NNESWW")
print("Конечное положение робота:", path)
print("Путь робота:", robot.path)
