class Point():
    def __init__(self, x:float, y: float, z: float,name: str):
        self.x = x
        self.y = y
        self.z = z
        self.coords = (x, y, z)
        self.name = name
    
    def __str__(self):
        return f"{self.name}: {self.coords}"

    def __abs__(self):
        return sum(i**2 for i in self.coords) ** 0.5
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z ,self.name + '+' + other.name)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z ,self.name + '-' + other.name)

    def __mul__(self, other):
        return abs(sel) * abs(other)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
    
    def convert_to_vector(self):
        return Vector(self.x, self.y, self.z, self.name)

class Vector(Point):
    def __init__(self, x:float, y: float, z:float, name: str):
        super().__init__(x, y, z, name)
    
    def __mul__(self, other: float):
        return Vector(self.x * other, self.y * other, self.z * other, self.name)

    def scal_mult(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def vec_mul(self, other):
        return Vector(self.y * other.z - other.y * self.z,
                      self.x * other.z - other.x * self.z,
                      self.x * other.y - other.y * self.x,
                      self.name + 'x' + other.name)

class Line(Vector):
    def __init__(self, p1: Point, p2: Point, name: str):
        self.p1 = p1
        self.p2 = p2
        l = p2 - p1
        self.l = l.convert_to_vector()
        super().__init__(l.x, l.y, l.z, name)
    
    def __str__(self):
        return f"({self.name}: ({self.l}) on ({self.p1}, {self.p2})"
    
    def __eq__(self, other):
        return self.l.scal_mult(self.other) == 0 