#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
R1= Rectangle(12, 10)
print("Rectangle area is :",R1.rectangle_area())
