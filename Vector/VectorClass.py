class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def magnitude(self):
        from math import sqrt
        return sqrt(self.a*self.a+self.b*self.b)
    def __eq__(self,other) -> bool:
        if [self.a,self.b]==[other.a,other.b]:
            return True
        return False
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)
    def __lt__(self,other):
        return self.magnitude() < other.magnitude()
    def __str__(self):
        return f"{self.a}x + {self.b}y"

