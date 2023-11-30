#exercise 2

#base class
class Person:
  #features defined with constructor
  def __init__(self):
    #self. features tied to object referencing 'self'
    self.name="bob"
    self.age= 20
    self.position = "worker"

  #method
  def display_info(self):
    print("persons name is ", self.name)
    print(f"persons age is{self.age}")

#inherits from base class
class Employee(Person):
  def addPosition(self):
    self.position = "worker"
    print("persons is ", self.position)

#calls methods
obj1 = Person()
obj1.display_info()
obj2= Employee()
obj2.addPosition()
