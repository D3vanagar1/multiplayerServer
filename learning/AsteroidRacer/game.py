# pyglet documentation: https://steveasleep.com/pyglettutorial.html


import pyglet
import random

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()
'''
class AsteroidWindow(pyglet.window.Window):
    def __init__(self):
        pass



asteroidCheese = AsteroidWindow()
'''


# learning about classes

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
class Cube(Square):
    def volume(self):
        face_area = super().area()
        return face_area * self.length


square = Square(4)
print(square.area())
print(square.perimeter())

cube = Cube(3)
print(cube.volume())
