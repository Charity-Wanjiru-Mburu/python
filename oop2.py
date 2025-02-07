# Using oop creat a class called cars that have the following attributes:
# Model , color and year of manufacturer .Implement constructor method and
# a method function that prints (my favorite cars is_ it is this in color -and manufactured)
# Create that instant of that class
class Cars:
    def __init__(self,model,year_manufacter,color):
        self.model=model
        self.color=color
        self.year_manufacter=year_manufacter
    def myfunction_cars(self):
        print(f"Hello, this is my favourite car {self.model} and it is {self.color} "
              f"in color which was manufactered in year {self.year_manufacter}")
# my instant class
mycar=Cars("Toyota",2024,"black")
mycar.myfunction_cars()