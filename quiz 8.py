#คำนวณพื้นที่ สามเหลี่ยม
class vehicle :
    def __init__(self,year,model,brand):
        self.year = year
        self.model = model
        self.brand = brand
        self.number_of_doors = true

        def get_info(self):
            return f"Brand {self.brand},Model: {self.model} , year:{self.year} "
class car(Vehicle):

    def __init__(self,brand,year,model,number_of_doors):
        super(). __init__(brand,model,year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"brand: {self.brand},Model:{self.model}, year:{self.year},number_of_doors {self.number_of_doors}"