# at first we define a class(parent) named Shape
class Shape:
    def __init__(self, length, width, height, diameter):
        self.length = length
        self.width = width
        self.height = height
        self.diameter = diameter


# defining a class(child) for a Square
# in the following classes it is not necessary to use super()... but I used it anyway!
class Square(Shape):
    def __init__(self, length, width, height, diameter):
        super().__init__(length, width, height, diameter)

    def space(self):
        return self.length ** 2

    def circumference(self):
        return 4 * self.length

    def draw(self):
        for i in range(self.length):
            for j in range(self.length):
                if i == 0 or i == (self.length - 1) or j == 0 or j == (self.length - 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


# defining a class(child) for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width, height, diameter):
        super().__init__(length, width, height, diameter)

    def space(self):
        return self.length * self.width

    def circumference(self):
        return 2 * (self.length + self.width)

    def draw(self):
        for i in range(self.length):
            for j in range(self.width):
                if i == 0 or i == (self.length - 1) or j == 0 or j == (self.width - 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


# defining a class(child) for Parallelogram
# in this class we use length as a larger side and width as a shorter side
class Parallelogram(Shape):
    def __init__(self, length, width, height, diameter):
        super().__init__(length, width, height, diameter)

    def space(self):
        return self.length * self.height

    def circumference(self):
        return 2 * (self.length + self.width)

    def draw(self):
        for i in range(0, self.width):
            for j in range(1, i + 1):
                print(" ", end="")
            for j in range(0, self.length):
                print(" *", end="")
            print()


# defining a class(child) for Diamond
# in this class we write a method to draw our diamond only with its height
class Diamond(Shape):
    def __init__(self, length, width, height, diameter):
        super().__init__(length, width, height, diameter)

    def space(self):
        return (1/2) * (self.height * self.diameter)

    def circumference(self):
        return 4 * self.length

    def draw(self):
        for i in range(1, self.height, 2):
            print(" " * (self.height // 2 - i // 2), "*" * i)
        for i in range(self.height, 0, -2):
            print(" " * (self.height // 2 - i // 2), "*" * i)


# defining a class(child) for Rhombus
class Rhombus(Shape):
    def __init__(self, length, width, height, diameter):
        super().__init__(length, width, height, diameter)

    def space(self):
        return self.length * self.height

    def circumference(self):
        return 4 * self.length

    def draw(self):
        for i in range(self.length):
            print(" " * (self.length - i) + " *" * self.length)


# defining some objects for our Shapes and printing
square_object = Square(5, 0, 0, 0)
print(square_object.space(), "\n", square_object.circumference(), "\n", square_object.draw())

rectangle_object = Rectangle(7, 5, 0, 0)
print(rectangle_object.space(), "\n", rectangle_object.circumference(), "\n", rectangle_object.draw())

parallelogram_object = Parallelogram(7, 5, 3, 0)
print(parallelogram_object.space(), "\n", parallelogram_object.circumference(), "\n", parallelogram_object.draw())

diamond_object = Diamond(3, 0, 5, 0)
print(diamond_object.draw(), "\n", diamond_object.circumference(), "\n", diamond_object.space())

rhombus_object = Rhombus(5, 0, 4, 0)
print(rhombus_object.draw(), "\n", rhombus_object.circumference(), "\n", rhombus_object.space())
