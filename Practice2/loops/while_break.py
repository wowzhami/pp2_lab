#Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


#Find first number divisible by 7
num = 1
while num <= 50:
    if num % 7 == 0:
        print(f"Found: {num} is divisible by 7")
        break
    print(f"Checking {num}...")
    num += 1
print()


#Find first even
n = 1
while True:
    if n % 2 == 0:
        print(f"Even: {n}")
        break
    n += 1



#Sum until 10
total = 0
while True:
    total += 1
    if total >= 10:
        print(f"Reached {total}")
        break


#Break when sum > 15
numbers = [4, 6, 3, 8, 2]
i = 0
total = 0
while i < len(numbers):
    total += numbers[i]
    print(f"Added {numbers[i]}, total: {total}")
    if total > 15:
        break
    i += 1