def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
#x: 10
#y: 20


def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
#Arguments before / are positional-only, and arguments after * are keyword-only