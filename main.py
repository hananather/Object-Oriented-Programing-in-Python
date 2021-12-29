class complex:
  def __init__(self, real = 0, imag = 0):
    self.real = real
    self.imag = imag
  
  def __add__(self, other):
    temp = complex(self.real + other.real,self.imag + other.imag)
    return temp
  
  def __sub__(self,other):
    temp = complex(self.real - other.real, self.imag - other.imag)
    return temp
  
    