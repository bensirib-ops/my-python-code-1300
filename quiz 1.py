class Circle:
    def __init__(self, radius):
        self.radius = radius
    

    # Method to get the area
    def get_area(self):
        return 3.14 * self.radius ** 2

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * 3.14 * self.radius


myCircle = Circle(5)
print(myCircle.get_area())       # Should print 50
print(myCircle.get_perimeter())  # Should print 30