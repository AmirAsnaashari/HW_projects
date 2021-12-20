class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def peri(self):
        return 2*(self.length+self.width)
    def space(self):
        return self.length*self.width
    def print_rect(self):
        print("perimeter:",self.peri())
        print("space:",self.space())
        print("width:", self.width)
        print("length:",self.length)

l = int(input())
w = int(input())
obj = Rectangle(l, w)
obj.print_rect()