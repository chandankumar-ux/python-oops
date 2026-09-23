class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Objects
c = Circle(5)
r = Rectangle(10, 4)
t = Triangle(6, 8)

print("Circle area:", c.area())
print("Rectangle area:", r.area())
print("Triangle area:", t.area())