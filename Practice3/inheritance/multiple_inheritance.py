class Phone:
    def call(self):
        print("Звоню...")
class Flashlight:
    def light_on(self):
        print("Свечу ярким светом!")
class Smartphone(Phone, Flashlight):
    pass
iphone = Smartphone()
iphone.call() 
iphone.light_on()




class Mother:
    def advice(self):
        print("Надень шапку!")
class Father:
    def advice(self):
        print("Ешь кашу!")
class Child(Mother, Father):
    pass
kid = Child()
kid.advice() #"Надень шапку!"