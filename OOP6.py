class Shark:
    animal_type = "fish" #Class variable
    counter = 99
    
    def __init__(self,animal_type):
        #Instance variable
        self.animal_type = animal_type

new_shark = Shark('a wet animal')
print(Shark.animal_type,Shark.counter) #Class variable
print(new_shark.animal_type) #Instance variable


class Person:
    a = 99
    b = 12.5
    
    def __init__(self,name,age,variable):
        self.name = name
        self.age = age
        self.variable = variable

dude1 = Person("John", 34, 5)

#We access Class variable

print(Person.a)
print(Person.b)

#We access instance variables
print(dude1.variable)

#We edit instance variable at runtime (on-the-go)
dude1.variable = 5555.5
print(dude1.variable)
