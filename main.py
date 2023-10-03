class Myclass:
    pass

class Dog:
    species = "Canis familiaris"

    def __int__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
       return f"{self.name} barks!"

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 2)

dog1 = Dog("Buddy", 5)
print(dog1.bark())

class GermanShepherd(Dog):
    def guard(self):
        return f"{self.name} is guarding"
    
gs_dog = GermanShepherd("Rex" , 3)
print(gs_dog.guard())