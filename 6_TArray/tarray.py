class TArray:
    def __init__(self, size=0):
        self.size = size
        self.data = [0] * size

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            result = TArray(self.size)
            result.data = [x + other for x in self.data]
            return result
        elif isinstance(other, TArray):
            if len(self) == len(other):
                result = TArray(self.size)
                result.data = [x + y for x, y in zip(self.data, other.data)]
                return result
            else:
                raise ValueError("Массивы должны иметь одинаковый размер")
        else:
            raise TypeError("Можно только добавить число или другой массив")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = TArray(self.size)
            result.data = [x * other for x in self.data]
            return result
        else:
            raise TypeError("Можно умножать только на число")

    def input_data(self):
        self.data = [float(input(f"Введите элемент {i + 1}: ")) for i in range(self.size)]

    def output_data(self):
        print(self)

    def find_max(self):
        return max(self.data)

    def find_min(self):
        return min(self.data)

    def sort(self):
        self.data.sort()

    def sum_elements(self):
        return sum(self.data)


arr = TArray(5)
arr.input_data()
print(f"Максимальный элемент: {arr.find_max()}")
print(f"Минимальный элемент: {arr.find_min()}")
arr.sort()
print("Отсортированный массив:", arr)
print(f"Сумма элементов: {arr.sum_elements()}")
arr2 = arr + 2
print("Массив + 2:", arr2)
arr3 = arr * 3
print("Массив * 3:", arr3)
