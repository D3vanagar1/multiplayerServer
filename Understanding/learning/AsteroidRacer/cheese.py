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



# 1. reverse a list
list1 = [100, 200, 300, 400, 500]
list1.append(600)
result = [500, 400, 300, 200, 100]
list1.reverse()
print(list1)


# 2. add two list by index
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list1.append(list2)

result = ['My', 'name', 'is', 'Kelly']
ziped = tuple(zip(list1, list2))
for e in eggman:
    print(e)
    