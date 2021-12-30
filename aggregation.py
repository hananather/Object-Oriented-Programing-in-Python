class Country:
  def __init__(self, name=None, population =0):
    self.name = name
    self.population = population

  def printDetails(self):
    print(self.name)
    print(self.population)

class Person:
  def __init__(self, name, country):
    self.name = name
    self.country = country 

  def printDetails(self):
    print(self.name)
    self.country.printDetails()


c = Country("Wales", 1500)
p = Person("Joe", c)
p.printDetails()


del p
print("")
c.printDetails()

