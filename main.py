from abc import ABC,abstractclassmethod

class Shape(ABC):
  @abstractclassmethod
  def area(self):
    pass
  
  @abstractclassmethod
  def peri(self):
    pass

class circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return (self.radius**2)*3.14
  
  def peri(self):
    return self.radius*2*3.14


c =circle(5)
print(c.radius)
print(c.area())
print(c.peri())



