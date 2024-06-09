import math


class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def surface_area(self):
        return 2 * math.pi * self.r * (self.r + self.h)

    def volume(self):
        return math.pi * self.r ** 2 * self.h


r = float(input("圆柱底面半径："))
h = float(input("圆柱高："))

cylinder = Cylinder(r, h)

print("圆柱体表面积：", cylinder.surface_area())
print("圆柱体体积：", cylinder.volume())
