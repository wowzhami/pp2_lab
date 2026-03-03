import re 
#1 
print(re.fullmatch(r"ab*", "abbb")) 


#2
print(re.fullmatch(r"ab{2,3}", "abbb")) 

#3
print(re.findall(r"[a-z]+(?:_[a-z]+)+", "da_da_da wz_ ala "))

#4
print(re.findall(r"\b[A-Z][a-z]+\b", "qwerty Uiop"))

#5
print(re.findall(r"^a.*b$", "wow awowb"))

#6
print(re.sub(r"[ ,.]", ";", "apple, banana. lemon"))

#7
print(re.sub(r"_([a-z])", lambda x : x.group(1).upper(), "hello_world"))

#8
print(re.findall(r"[A-Z][a-z]*", "AlmatyKbtu"))

#9
print(re.sub(r"([A-Z])", r" \1", "AlmatyKbtu"))

#10
print(re.sub(r"([A-Z])", lambda x: "_" + x.group(1).lower(), "AaaBbbCcc").lstrip("_"))