class Vector2D:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def scale(self, factor):
        return Vector2D(self.x * factor, self.y * factor)

v1 = Vector2D(2, 3)
v2 = Vector2D(1, 4)
v3 = v1.add(v2)
v4 = v1.scale(2)

print("2) Vector2D:")
print("Қосу:", v3.x, v3.y)
print("Масштабтау:", v4.x, v4.y)
print("Қосымша:", v4.x, v4.y)
print("Қосымша2:", v4.x, v4.y)
print("Қосымша3:", v4.x, v4.y)
print("Қосымша3:", v4.x, v4.y)