class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int):
            return Vector(self.x + other, self.y + other, self.z + other)
    def __truediv__(self, other):
        if isinstance(other, int):
            return Vector(self.x / other, self.y / other, self.z / other)

        


    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'
            
    



n = int(input())
cords = []
for i in range (n):
    cords.append(0) 
for i in range (n):
    cords[i] = str(input())


vectors = []
for i in range (n):
    vectors.append(0) 
for i in range (n):
    vectors[i] = Vector(int(cords[i][1]), int(cords[i][4]), int(cords[i][7]))

summ = 0
for i in range (n):
    summ = vectors[i] + summ

mass_centre = summ / n
print(str(mass_centre))
