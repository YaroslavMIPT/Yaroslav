import math

class Rational:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = (self.x * other.y) + (other.x * self.y)
        y = self.y * other.y
        t = math.gcd(x, y)
        return Rational(x//t, y//t)

    def __sub__(self, other):
        x = (self.x * other.y) - (other.x * self.y)
        y = self.y * other.y
        t = math.gcd(x, y)
        return Rational(x//t, y//t)

    def __mul__(self, oth):
        x = (self.x * oth.x)
        y = self.y * oth.y
        t = math.gcd(x, y)
        return Rational(x//t, y//t)

    def __truediv__(self, oth):
        x = (self.x * oth.y)
        y = self.y * oth.x
        t = math.gcd(x, y)
        return Rational(x//t, y//t)

    def __str__(self):
        return "{0}/{1}".format(self.x, self.y)

    def __float__(self):
        return self.x / self.y

#tests
a = Rational(1, 2)
b = Rational(1, 3)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(float(a / b))

print("Тесты из условия:")
r1 = Rational(1, 2)
r2 = Rational(-1, 2)

print(r1 * r2)    # -1/4
print(float(r1))  # 0.5