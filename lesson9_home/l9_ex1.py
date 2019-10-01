class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter = 2*self.length + 2*self.width
        return perimeter

    def area(self):
        area = self.width * self.length
        return area

some_rectangle = Rectangle(4, 3)

print(some_rectangle.perimeter())
print(some_rectangle.area())