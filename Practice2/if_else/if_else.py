#The else statement must come last. You cannot have an elif after an else.
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")


#compare number
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#even/odd number
  number = 7
  print(f"Число: {number}")
  if number % 2 == 0:
      print("even")
  else:
      print("odd")
  print()

  #Website access
  age = 16
  print(f"Age: {age}")
  if age >= 18:
      print("Access granted")
  else:
      print("Access denied")
  print()

  #Password check
  input_password = "12345"
  correct_password = "qwerty"
  print(f"Entered password: {input_password}")
  if input_password == correct_password:
      print("Password is correct")
  else:
      print("Password is incorrect")
  print()