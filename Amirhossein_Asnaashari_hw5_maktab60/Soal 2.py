import math


class Sphere:
    def __init__(self, r):
        self.r = r

    def volume(self):
        return (4/3) * math.pi * self.r**3

    def space(self):
        return 4 * math.pi * self.r**2

    def zero(self):
        if self.r <= 0:
            raise ValueError('Only positive integers are allowed')

    try:
        zero()

    except ValueError:
        print("Error: amount of Radius is invalid")


n = Sphere(5)
print(n.space(), n.volume(), n.zero())
