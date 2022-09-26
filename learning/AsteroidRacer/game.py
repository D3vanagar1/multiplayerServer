# pyglet doccumentation: https://steveasleep.com/pyglettutorial.html


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
        super().__init__(length, width)

square = Square(4)
print(square.area())
