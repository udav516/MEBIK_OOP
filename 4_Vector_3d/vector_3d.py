class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector3D(self.x * other, self.y * other, self.z * other)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(Vector3D.__add__(v1, v2))
print(Vector3D.__sub__(v1, v2))
print(Vector3D.__mul__(v1, v2))
print(Vector3D.__mul__(v1, 2))
