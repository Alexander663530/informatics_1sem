class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int):
            return Vector(self.x + other, self.y + other, self.z + other)

    def sin(self, other):
        if isinstance(other, Vector):
            scalar_mul = self.x * other.x + self.y * other.y + self.z * other.z
            
            absol1 = (self.x**2 + self.y**2 + self.z**2)**0.5
            absol2 = (other.x**2 + other.y**2 + other.z**2)**0.5
            
            cos = scalar_mul / (absol1 * absol2)

            sinus = (1 - cos**2)**0.5
            return sinus
        


    def __str__(self):
        return f'x = {self.x} y = {self.y} z = {self.z}'


n = int(input())
cords = []
for i in range (n):
    cords.append(0) 
for i in range (n):
    cords[i] = str(input())


vershiny = []
for i in range (n - 2):
    for k in range (i + 1, n - 1):
        for l in range (k + 1, n):
            vershiny.append([cords[i], cords[k], cords[l]])


vx = []
vy = []
vz = []


for i in range (len(vershiny)):
    vx.append([int(vershiny[i][1][1]) - int(vershiny[i][0][1]), int(vershiny[i][2][1]) - int(vershiny[i][0][1])])
    vy.append([int(vershiny[i][1][4]) - int(vershiny[i][0][4]), int(vershiny[i][2][4]) - int(vershiny[i][0][4])])
    vz.append([int(vershiny[i][1][7]) - int(vershiny[i][0][7]), int(vershiny[i][2][7]) - int(vershiny[i][0][7])])


vectors = []
for i in range (len(vershiny)):
    vectors.append([Vector(vx[i][0], vy[i][0], vz[i][0]), Vector(vx[i][1], vy[i][1], vz[i][1])])
    

square = []
for i in range (len(vectors)):
    square.append(0.5 * abs(vectors[i][0]) * abs(vectors[i][1]) * vectors[i][0].sin(vectors[i][1]))
print(max(square))
    
    



