""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class vehicle:
    def __init__(self,model,year,brand):
        self.model = model
        self.year = year
        self.brand = brand
        self.number_of_doors = true
        
       
        def get_info(self):
            return f"Brand: {self.brand},Model: {self.model} , year:{self.year}"

class car(Vehicle):

    def __init__(self,brand,year,model,number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Brand:  {self.brand},Model:{self.model} , year:{self.year},number of doors : {self.number_of_doors}"

    