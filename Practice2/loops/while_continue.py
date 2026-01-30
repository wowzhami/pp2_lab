#Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Only even numbers
num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
        continue
    print(num)



# Skip negatives
nums = [5, -1, 3, -2, 4]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1



# Skip vowels
word = "hello"
i = 0
while i < len(word):
    if word[i] in "aeiou":
        i += 1
        continue
    print(word[i])
    i += 1