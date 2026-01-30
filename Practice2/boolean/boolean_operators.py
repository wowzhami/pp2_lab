print("True and True =", True and True)      # True
print("True and False =", True and False)    # False
print("False and True =", False and True)    # False
print("False and False =", False and False)  # False



x = 0
y = 10
result_and = (x != 0) and (y / x > 2)  
print(f"(x != 0) and (y / x > 2) = {result_and}")

#not > and > or
result1 = True or False and not True
result2 = (True or False) and not True
print(f"True or False and not True = {result1}")
print(f"(True or False) and not True = {result2}")
