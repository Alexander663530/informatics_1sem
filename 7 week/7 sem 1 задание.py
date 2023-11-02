class Vector:
    def __init__(self, x, y, z):
        if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float) and isinstance(z, int) or isinstance(z, float):
            self.x = x
            self.y = y
            self.z = z


    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5


    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.x)


    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.x)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)


    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


cord1 = str(input())
cord2 = str(input())
#{1, 2, 3}
v1 = Vector(int(cord1[1]), int(cord1[4]), int(cord1[7]))
v2 = Vector(int(cord2[1]), int(cord2[4]), int(cord2[7]))

a = int(input())


summ = v1 + v2
sub = v1 - v2
scalar_mul = v1 * v2
mul1 = v1 * a
mul2 = v2 * a


print(str(summ))
print(str(sub))
print(str(scalar_mul))
print(str(mul1))
print(str(mul2))
