#With the while loop we can execute a set of statements as long as a condition is true
# ExampleGet your own Python Server
# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1


#Sum of numbers from 1 to 10
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Total sum: {total}")
print()



#Decreasing counter
counter = 5
while counter > 0:
    print(counter)
    counter -= 1
print("Blast off!")
print()


#Processing items in a list
shopping_list = ["milk", "eggs", "bread", "butter"]
index = 0
while index < len(shopping_list):
    print(f"Item {index + 1}: {shopping_list[index]}")
    index += 1


#Count from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
print()
