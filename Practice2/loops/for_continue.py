#Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#  Skip even numbers
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)



#  Skip "skip"
words = ["hello", "skip", "world"]
for word in words:
    if word == "skip":
        continue
    print(word)

# Only show > 3
nums = [1, 4, 2, 5, 3]
for num in nums:
    if num <= 3:
        continue
    print(num)

# Skip spaces
text = "a b c"
for char in text:
    if char == " ":
        continue
    print(char)