
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age) #Emil 18
print(p2.name, p2.age)  #Tobias 25



class Person:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet() #Hello, my name is Emil



class Calculator:
  def add(self, a, b):
    return a + b
  def multiply(self, a, b):
    return a * b
calc = Calculator()
print(calc.add(5, 3)) #8
print(calc.multiply(4, 7))  #28



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")
p1 = Person("Linus", 25)
p1.celebrate_birthday() #Happy birthday! You are now 26
p1.celebrate_birthday() #Happy birthday! You are now 27
