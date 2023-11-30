#exercise 1

#base class
class Person:
  #features defined with constructor
  def __init__(self):
    #self. features tied to object referencing 'self'
    self.name="bob"
    self.age= 20

  #method
  def display_info(self):
    print("persons name is ", self.name)
    print(f"persons age is{self.age}")

#calls methods
obj = Person()
obj.display_info()
