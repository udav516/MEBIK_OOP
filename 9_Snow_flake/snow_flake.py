class SnowFlake:
    def __init__(self, side):
        if side % 2 == 0:
            raise ValueError("Длина сторон должна быть нечетной")
        self.side = side
        self.matrix = [['-' for _ in range(side)] for _ in range(side)]
        self.initialize_snowflake()

    def initialize_snowflake(self):
        for i in range(self.side):
            for j in range(self.side):
                if i == j or i + j == self.side - 1 or abs(i - j) == (self.side - 1) // 2:
                    self.matrix[i][j] = '*'

    def thaw(self, steps):
        for _ in range(steps):
            self.matrix[0] = ['-'] * self.side
            self.matrix[-1] = ['-'] * self.side
            for i in range(1, self.side - 1):
                self.matrix[i][0] = '-'
                self.matrix[i][-1] = '-'
            self.side -= 2

    def freeze(self, n):
        self.side += 2 * n
        new_matrix = [['-' for _ in range(self.side)] for _ in range(self.side)]
        for i in range(self.side):
            for j in range(self.side):
                if i == j or i + j == self.side - 1 or abs(i - j) == (self.side - 1) // 2:
                    new_matrix[i][j] = '*'
        self.matrix = new_matrix

    def thicken(self):
        new_matrix = [['-' for _ in range(self.side)] for _ in range(self.side)]
        for i in range(self.side):
            for j in range(self.side):
                if self.matrix[i][j] == '*':
                    new_matrix[i][j] = '*'
                    if i > 0:
                        new_matrix[i - 1][j] = '*'
                    if i < self.side - 1:
                        new_matrix[i + 1][j] = '*'
        self.matrix = new_matrix

    def show(self):
        for row in self.matrix:
            print(''.join(row))


snowflake = SnowFlake(7)

print("Первая снежинка:")
snowflake.show()
print()

snowflake.thaw(2)
print("Снежинка после оттаивания в 2 этапа:")
snowflake.show()
print()

snowflake.freeze(1)
print("Снежинка после замораживания 1 шаг:")
snowflake.show()
print()

snowflake.thicken()
print("Снежинка после загустения:")
snowflake.show()
print()
