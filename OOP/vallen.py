# challenge create a Car class with variables: color, and model
# with method function displays all parts of Car
class car:
  model = "dinosaur car"
  color = "rainbow"
  def display(self):
    print (self.model + self.color)
  
#dinosaur = car()
#dinosaur.display()



'''
Challenge 1: make Burger class:
  - meat variable (chicken, beef, ham)
  - extaCheese = True/False
* makea  constructor for this object
  * with a varaible named after you 
'''
class hamburga:
  # constructor
  def __init__(self, meat, cheese, veggies):
    self.meat = meat
    self.cheese = cheese
    self.veggies = [veggies]

  def addveggies(self, veggies):
    self.veggies.append(veggies)

  def __del__(self):
    print(self.meat + " burger has been eaten with a eating  ")

hamburga1 = hamburga("chicken", True, ["lettuce", "cucumber"])
hamburga2 = hamburga("cheese", True, ["tomotoes", "pickles"])
#print(hamburga1.meat)
#print(hamburga2.cheese)


'''
Challenge 2: write a function that adds veggies burger
and add destructor (_del_) that says "Burger has been eaten"
'''



'''
* Challenge:
  - Create an Employee class:
      - name
      - salary (number in the thosands)
      - role (Manager, Cashier,etc.)
  * changeSalary function(amount)
     - changes the salary to the given ammount
'''
class Company:
  def __init__(self, name):
    self.name = name
class Employee(Company):
  # constructor
  def __init__(self, meat, blood, salary,role,Cname):
    self.meat = meat
    self.blood = blood
    self.salary = salary
    self.role = role
    Company.__init__(self,Cname)
  def changeSalary(self, Newsalary):
    self.salary = Newsalary



Bill = Employee(26,64,123456789, "Cashier", "Chicken")
print(Bill.name)
Bill.changeSalary(1000)
print(Bill.salary)




'''
Challenge make Company class to be the parent of your employee class (already made)
  - company has name, and about(what they do)
  - employee has to set the company name and proj
'''



class Pokemon:
  def __init__(self, type, name):
    self.type = type
    self.Pname = name


class Trainer(Pokemon):
  def __init__(self, tName, level, Pokemon_name, Pokemon_type):
    self.tname = tName
    self.level = level
    Pokemon.__init__(self, Pokemon_type, Pokemon_name)



Pikachu = Pokemon("electric", "Pikachu")
Ash = Trainer("Ash", 15, Pikachu.Pname, Pikachu.type)


print(Ash.Pname)



'''
Review:

- Challenge 1:
  * create Racecar class
    - constructor: set the model, color, top_speed, weardown_time
    -  1 method function: weardown() -> reduces the value of weardown_time 1 sec at a time
        weardown_time -= 1

    - 1 method function: race() -> runs weardown() in a while loop


    - create Racecar instance: Lambo = Racecar("Lambo", "red", 250, 50)

'''

class racecar:
  
  matrix = [ [0 for j in range(0,10)] for i in range(0,10)]

  # constructor
  def __init__(self, newmodel, newColor, weardowntime, sped):
    self.model = newmodel
    self.color = newColor
    self.weardowntime = weardowntime
    self.sped = sped

  def weardown(self):
    self.weardowntime -= 1  

  def race(self):
    while self.weardowntime > 0:
      self.weardown()
   



  
    

racecar1 = racecar("ethan", "big_dum_dum", 10000000,9)
racecar1.weardown()
racecar1.race()
print("weardown time:" + str(racecar1.weardowntime))