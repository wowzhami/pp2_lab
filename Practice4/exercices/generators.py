#1
def sq(num):
    for i in range(num+1):
        yield i*i
n = int(input()) 
for i in sq(n):
    print(i)
#2
def even(num):
    for i in range(0, num+1, 2):
        yield i
a = int(input())
g = even(a) 
print(next(g), end="")
for i in g:
    print(f",{i}", end="") 
print()
#3
def div(n):
    for i in range(0, n+1, 12):
        yield i 
x = int(input())
z = div(x) 
for i in z:
    print(i)
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
c = int(input())
k = int(input())
p = squares(c, k)
for i in p:
    print(i) 
#5
def down(n):
    for i in range(n, -1, -1):
        yield i
q = int(input())
w = down(q)
for i in w:
    print(i)