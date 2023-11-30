#exercise 3
adultEmployeeCount = 0
minorEmployeeCount = 0

#base class
class Person:
  def __init__(self, name, age, position): #features defined with constructor
    #self. features tied to object referencing 'self'
    self.name= name
    self.age= age
    self.position = position

  #method
  def display_info(self):
    print("persons name is ", self.name)    
    print(f"persons age is {self.age}")
    print("persons is ", self.position)
    print("------------------------")

  #method
  def age_check(self):
        global adultEmployeeCount
        global minorEmployeeCount
        if self.age >= 18:
            adultEmployeeCount += 1
        else:
            minorEmployeeCount += 1

class Company:
  def __init__(self, employee=[]): #constructor & list for employees
    self.employee = employee

  def display_all_info(self):
    print(f"Total Info: ")
    for i in self.employee:
      i.display_info()
      i.age_check()
    print(f"Adult employees: {adultEmployeeCount}")
    print(f"Minor employees: {minorEmployeeCount}")
    print(f"total empoyees: ", len(self.employee))


#instances of employees created
employee1 = Person("Bob", 18, "Worker")
employee2 = Person("Alice", 30, "Manager")
employee3 = Person("Charlie", 16, "Intern")
employee4 = Person("David", 23, "Supervisor")
employee5 = Person("Eva", 28, "worker")

#list passes instance to Company constructor
employeeData = Company ([employee1, employee2, employee3, employee4, employee5])
employeeData.display_all_info() #calls method
