def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument




def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")    #I am from Sweden
my_function("India")     #I am from India
my_function()            #I am from Norway
my_function("Brazil")    #I am from Brazil



def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")
#I have a dog
#My dog's name is Buddy