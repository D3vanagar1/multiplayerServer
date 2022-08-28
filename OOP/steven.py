
# challenge create a Car class with variables: color, and model
# with method function displays all parts of Car
class car: #class declaration 
  color = "red"
  model = "Fords Focus"
  size = "69ft"
  def display(self, a): 
    print("Car color: " + self.color + " Car model: " + self.model + " Car size : " + self.size + a)


toyota= car()
toyota.display(" job")



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
  #constructor
  def __init__(self, name, task):
    self.name = name
    self.task = task

  def show(self):
    print("The goal of the company is: ", self.task)

class Kar(Company):
  def __init__(self, salary, role, score, cName, task):
    self.salary = salary
    self.role = role
    self.score = score
    Company.__init__(self, cName, task)
    

  def ChangeSalary(self, NewSalary):
    self.salary = NewSalary


Googoo = Kar(696969696969000, "noob",69,"Gus",'how to become poor')
print(Googoo.name)
Googoo.ChangeSalary(10000)
print(Googoo.task)



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
class Racecar:
  matrix = [ [0 for j in range(0,10)] for i in range(0,10)]

  # constructor
  def __init__(self, model, color, top_speed, weardown_time):
    self.model = model
    self.color = color
    self.top_speed = top_speed
    self.weardown_time = weardown_time

  def weardown(self):
    self.weardown_time -= 1 # hint: the answer is in the challenge description

  def race(self):
    while self.weardown_time>0:
      self.weardown()
        
        


poopypants = Racecar("poopypants", "Rainbow", 250, 50)
poopypants.weardown()
poopypants.race()
print("weardown time:" + str(poopypants.weardown_time))


def




