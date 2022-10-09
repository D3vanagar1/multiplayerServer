# make an empty class where we set the caption of the mass murder

# gun class
# self.caption = "hambuga"
class mass_muda:
     __init__(self)
     self.caption = "hambuga"

vallen = mass_muda()
vallen.caption = "ajvieas;ifamsvasl;imdsfvj;als,iafs;ijx.alisdj,;fajivej;failesfjb;eijfiej;fl;esfujl;-098q074563=-++_0e9r=-03950954-89*&&@^%(J%I_)#(J_GE*h-90-8j4-38="

vallen2 = mass_muda()

print(vallen.caption)
print(vallen2.caption)


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
