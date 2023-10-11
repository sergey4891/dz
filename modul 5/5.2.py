from math import hypot

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self): # метод вычесления вектора
        return hypot(self.x, self.y)
p1 = Point(2,2)
print(p1.abs())
