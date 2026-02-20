#ITER 
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit)) #apple
print(next(myit)) #banana
print(next(myit)) #cherry

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter)) #1
print(next(myiter)) #2
print(next(myiter)) #3
print(next(myiter)) #4
print(next(myiter)) #5 

#STOPITERATION 
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x) #до 20(вкл) выведет



#GENERSTION
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1
ctr = fun(5)
for n in ctr:
    print(n)
#1
#2
#3
#4
#5


def fun():
    yield 1            
    yield 2            
    yield 3            
for val in fun(): 
    print(val)
#1
#2
#3
#crate generarion
# Квадраты чисел от 1 до 5
squares = (x*x for x in range(1, 6)) # in bracets
for s in squares:
    print(s)