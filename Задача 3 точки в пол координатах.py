import math


class Point:
    def __init__(self, r, phi):
        self.r = r
        self.phi = phi

    def __add__(self, other):
        x1 = self.r * math.cos(math.radians(self.phi))
        y1 = self.r * math.sin(math.radians(self.phi))
        x2 = other.r * math.cos(math.radians(other.phi))
        y2 = other.r * math.sin(math.radians(other.phi))

        x = x1 + x2
        y = y1 + y2

        r = math.sqrt(x ** 2 + y ** 2)
        phi = math.degrees(math.atan2(y, x))
        return Point(r, phi)

    def __str__(self):
        return f"(r = {self.r}, φ = {self.phi})"

    def __eq__(self, other):
        while self.phi > 360:
            self.phi -= 360
        while other.phi > 360:
            other.phi -= 360
        return self.r == other.r and self.phi == other.phi


def from_cartesian(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    phi = math.degrees(math.atan2(y, x))
    return Point(r, phi)


p = Point(r=10, phi=30)
print(p)

p1 = Point(r=1, phi=0)
p2 = Point(r=1, phi=90)
p3 = p1 + p2  # точка с r = 1.41 (примерно) и phi = 45
print(p3)

p1 = Point(1, 120)
p2 = Point(1, 480)
print(p1, p2)
print(p1 == p2)  # True

p = Point(1, 10)
print(p)  # (r = 1, φ = 10)
