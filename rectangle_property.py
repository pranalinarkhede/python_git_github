# property concept in python

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        print("Width : ",self._width)       
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        print("Height : ",self._height)   
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def perimeter(self):
        print("Perimeter of rectangle : ",2*(self._height + self._width))
        
    @property
    def area(self):
        print("Area of rectangle : ",self._height * self._width)


r = Rectangle(32, 48)
r.width
r.height
r.perimeter
r.area