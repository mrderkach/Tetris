class Point:
    def __init__(self, *s):
        if len(s) == 1:
            self.x = s[0][0]
            self.y = s[0][1]
        else:
            self.x = s[0]
            self.y = s[1]
            
    def is_belong(self, p):
            points = p.points
            for i in range(len(points) - 1, - 1, -1):
                if Vector(points[i], points[i - 1]) ** Vector(points[i], self) * Vector(points[i - 1], points[i - 2]) ** Vector(points[i - 1], self) < 0:
                    return 0
            return 1    
        
    def xy(self):
        return (self.x, self.y)

class Vector(Point):
    def __init__(self, a, b):
        if type(a) == Point:
            self.x = b.x - a.x
            self.y = b.y - a.y
        else:
            super().__init__(a, b)
            
    def __mul__(self, other):     #Only dotProduct
        return self.x * other.x + self.y * other.y
    
    def __pow__(self, other):     #Only crossProduct
        return self.x * other.y - self.y * other.x

class Polygon:
    def __init__(self, s):
        self.points = s
        
    def first(self):
        return self.points[0].x - 20, self.points[0].y
