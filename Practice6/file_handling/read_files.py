f = open("demofile.txt")
print(f.read())

with open("demofile.txt") as f:
  print(f.read())
  print(f.read(5)) # hello


f = open("demofile.txt")
print(f.readline())
f.close()