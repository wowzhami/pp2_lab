#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

#  Stop when total > 10
total = 0
for num in [3, 5, 7, 2]:
    total += num
    if total > 10:
        break
    print(total)



#  Find capital letter
text = "hello World"
for char in text:
    if char.isupper():
        print(f"Found: {char}")
        break


#  Stop at empty string
words = ["cat", "dog", "", "bird"]
for word in words:
    if word == "":
        break
    print(word)


#  Stop at 3
for i in range(5):
    if i == 3:
        break
    print(i)
