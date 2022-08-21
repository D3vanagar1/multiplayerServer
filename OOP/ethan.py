# challenge create a Car class with variables: color, and model
# with method function displays all parts of Car

        

class car: #Class declaration
  color = "rainbow"
  model = "hamburger"
  def display(self): #Instance method
    print( "the color is " + self.color + " the model is " + self.model)

  def changeColor(self, newColor):
    self.color = newColor



wheels = car() # create an instance
#wheels.changeColor("blue")
#wheels.display()


# create 2 instances (Car1 and Car2). write method function to change the color of the car


'''
Challenge 1: make Burger class:
  - meat variable (chicken, beef, ham)
  - extaCheese = True/False
* makea  constructor for this object
  * with a varaible named after you 
'''
class hamburger:
  # constructor
  def __init__(self, meat, veggies, cheetoes):
    self.meat = meat
    self.veggies = veggies
    self.cheetoes = cheetoes
    

  
  def addSkill(self, veggies):
    self.veggies.append(veggies)


  def __del__(self):
    print(" you ate the bruger ")
 
    
hamburger1 = hamburger("steak", "mushroom", True)
newBurger = hamburger("chicken", ["lettuce", "tomatoes"], True)

print(newBurger.veggies)

  
    
  
    

'''
* Challenge:
  - Create an Employee class:
      - name
      - salary (number in the thosands)
      - role (Manager, Cashier,etc.)
  * addDevilfunction(amount)
     - changes the salary to the given ammount
'''

class Company:
  #constructor
  def __init__(self, name, proj):
    self.name = name
    self.proj = proj

  def show(self):
    print("The goal of the company is: ", self.proj)
    
class worker(Company):
  def __init__(self, name, salary, role, Devil, cName, proj):
    Company.__init__(self,cName, proj)
    self.name = name
    self.salary = salary
    self.role = role
    self.Devil = Devil
    
  def addDevil(self, Devil):
    self.Devil = Devil
    self.Devil.append(Devil)


  def __del__(self):
    print(" u summoned a Devil ")
 
    
worker1 = worker("bob", "10", "summonor", "no Devils summoned", "Mcdonalds", "flips bugers")
newdworker = worker("bob", "10", "summonor", "1 Devil summoned", "Mcdonalds", "makes fries") 

c = Company("the box", "box god")
e = worker("Steve", 9999, "cashier", "1 devil summoned", c.name, c.proj)

print("Welcome to", c.name)
print("Here ", e.name, "Is working on ", e.proj)




'''
Challenge make Company class to be the parent of your employee class (already made)
  - company has name, and about(what they do)
  - employee has to set the company name and proj
'''

















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



class racecar:
  # constructor
  def __init__(self, model, color, top_speed, weardown_time):
    self.model = model
    self.color = color
    self.top_speed = top_speed
    self.weardown_time = weardown_time

  def weardown(self):
    self.weardown_time -= 1

    
  def race(self):
    while self.weardown_time > 0:
      self.weardown()

    

racecar1 = racecar("The devil", "Redblack", 1000000000000000000000000000, 100)
racecar1.weardown()
racecar1.race()

print(racecar1.weardown_time)
