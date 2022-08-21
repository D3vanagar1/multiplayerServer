# OOP: Object-Oriented Programming
# classes, instances, methods

class fruits: #Class declaration
  Name = "Apple"
  No = "A1"
  Number = 10
  def display(self): #Instance method
    print(self.Name, self.No)

  def concat(self):
    print(self.Name + self.No)

  def foobar(self):
    self.No += "Quandale Dingel"

  def addsFruit(self):
    self.Number += 1

# bad practice
def temp(fruit):
  print(fruit.Name)

Fruity = fruits()# create an instance
Fruity.Name = "Banana"
print("Name of fruit: " + Fruity.Name)
Fruity.foobar()
print(Fruity.No)
Fruity.addsFruit()
print(Fruity.Number)

temp(Fruity)
#Fruity.display()
#Fruity.concat()


'''
Challenge 1:
create a Car class with variables: color, and model
with the method, the function displays all parts of the car object

Challenge 2:
create 2 instances (Car1 and Car2). write method function to change the color of the car
'''



class Ninja:
  
  matrix = [ [0 for j in range(0,10)] for i in range(0,10)]

  # constructor
  def __init__(self, newName, newColor, skills, score=0):
    self.name = newName
    self.color = newColor
    self.skills = [skills]
    self.score = score

  def addSkill(self, skill):
    self.skills.append(skill)

  def intializeMatrix(self):
    for i in range(0,10):
      for j in range(0,10):
        self.matrix[i][j] = 1

  #ninja destructor
  #def __del__(self):
  #  print(self.name + " has died with a score of " + str(self.score))
    #del matrix
  
    

Ninja1 = Ninja("Ethan", "Red", "hamburger")
Ninja2 = Ninja("Vallen", "Blue", "Expert")
Ninja1.addSkill("watching spongebob")
Ninja1.intializeMatrix()
print(Ninja1.skills)
print(Ninja1.matrix)
#del Ninja1
#print(Ninja2.name)

# Construcutors and Destructors

#  Constructor: special type of function that is automatically called when object is created ( myObject = Example() )
#    __new__(self)


'''
Challenge 1: make Burger class:
  - meat variable (chicken, beef, ham)
  - extaCheese = True/False
* makea  constructor for this object
  * with a varaible named after you 

Challenge 2: write a function that adds veggies burger
and add destructor (_del_) that says "Burger has been eaten"
'''



#inheritence

#parent class
'''
class Company:
  #constructor
  def __init__(self, name, proj):
    self.name = name
    self.proj = proj

  def show(self):
    print("The goal of the company is a big baby class
class Employee(Company):
  #constructor
  def __init__(self, eName, sal, cName, proj):
    Company.__init__(self,cName,proj)
    self.name = eName
    self.sal = sal

  def showSal(self):
    print("The salary of ", self.name, "is ", self.sal)


c = Company("Stark Industries", "Ironman")
e = Employee("Anthony", 9999, c.name, c.proj)

print("Welcome to", c.name)
print("Here ", e.name, "Is working on ", e.proj)
'''

'''
Challenge make Company class to be the parent of your employee class (already made)
  - company has some attributes: name, and about(what they do)
  - employee has to set the company name and proj
'''

#Access Modifiers (Public, Protected, Private)
# Public: can access outside of the class
# Protected: access outside of class if it is the child's class
#Private: No access outside


#parent class
class Company:
  #constructor
  def __init__(self, name, proj):
    self.name = name # public
    self._proj = proj # protected

  def show(self):
    print("The goal of the company is: ", self._proj)

#ethan is a big baby class
class Employee(Company):
  #constructor
  def __init__(self, eName, sal, cName, proj):
    Company.__init__(self,cName,proj)
    self.name = eName # public member
    self.__sal = sal # private member

  def changeProject(self, newProj):
    self._proj = newProj

  def showSal(self):
    print("The salary of ", self.name, "is ", self.__sal)


c = Company("Stark Industries", "Ironman")
e = Employee("Anthony Edwards", 9999, c.name, c._proj)

print("Welcome to", c.name)
print("Here ", e.name, "is working on ", e._proj)

e.__sal = 2000
#print("Now " + e.name + " is working on " + e._proj)


'''
Review:

- Challenge 1:
  * create Racecar class
    - constructor: set the model, color, top_speed, weardown_time
    -  1 method function: weardown() -> reduces the value of weardown_time 1 sec at a time
        weardown_time -= 1

    - 1 method function: race() -> runs weardown() in a for loop


    - create Racecar instance: Lambo = Racecar("Lambo", "red", 250, 50)

'''