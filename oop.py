# object oriented programming
from copyreg import constructor


class Person:
    def __init__(self,name,age):
        # this is a constructor method
        # it takes two parameters and initialize as attributes
        self.name=name
        self.age=age
    def myfunction(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")
        # this is a method function
#react an object or an instance of a class
myobj=Person("Charity",13)
myobj.myfunction()
myobj2=Person("Sharon","19")
myobj2.myfunction()
myobj3=Person("Alice",16)
myobj3.myfunction()
myobj4=Person("Prosper",23)
myobj4.myfunction()
myobj5=Person("Maggy",18)
myobj5.myfunction()