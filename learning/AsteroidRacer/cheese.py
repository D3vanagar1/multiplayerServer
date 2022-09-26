# make an empty class where we set the caption of the mass murder

# gun class
# self.caption = "Cheese"

class gun:
    def __init__(self):
        self.caption = "Cheese"

ethan = gun()
ethan.caption = "cheetos"

ethan2 = gun()

print(ethan.caption)
print(ethan2.caption)

# task add cube class, has volume function


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
