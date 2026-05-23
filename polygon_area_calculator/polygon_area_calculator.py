import abc
import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height
        
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt((self.width**2) + (self.height**2))

    def get_picture(self):
        rows = []
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        for i in range(self.height):
            rows.append('*' * self.width)
        return '\n'.join(rows) + '\n'      
    
    def get_amount_inside(self, square):
        return (self.width // square.width * self.height // square.height)
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def __str__(self):
        return f'Square(side={self.width})'

picture = Rectangle(49, 49)
print(picture.get_picture())