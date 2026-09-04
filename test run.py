def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")#กลับไปมอง print(f"Hello, {name}! Nice to meet you.") 
greet_person("Bob")#กลับไปมอง print(f"Hello, {name}! Nice to meet you.") 
greet_person("Charlie")#กลับไปมอง print(f"Hello, {name}! Nice to meet you.") 
print()

#example 3
#15
#70
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3) #กลับไปรันบรรทัดที่ def calculate_rectangle_area(length, width):
calculate_rectangle_area(10, 7)#กลับไปรันบรรทัดที่ def calculate_rectangle_area(length, width):

#example 1 part3
#5 + 3 = 8
#10 + 7 = 17
#sum of both result: 25

def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3) #sum 1 = 8
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()

#example 2 
#circle with radius 5
#

def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    volumn = 4.0 / 3 * pi * radius ** 3
    return area, circumference, volumn #return ข้อมูลมากกว่า 1 ค่า

print("Circle calculations:") #return มากกว่า 1 ค่าได้
radius = 5
area, circumference, volumn = get_circle_info(radius) #เอาตัวแปรมาเก็บที่นี่
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print(f"Volumn : {volumn:.2f}")
print()

#example1 part4
#using default parameter
# Hello Mr./Ms. smith !
#Hello Dr. john !
#Hello prof. brown !

def greet_with_title(name, title="Mr./Ms."):#ถ้าไม่ส่งจะขี้นMr./Ms.
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

#Example2
#Multiple default parameters:
#Profile: ALice , Age:18 , country:unknown
#Profile: Bob , Age:25, country:unknown
#Profile: Charlie ,Age:30, country:USA

def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()

#เขียน function ชื่อ convert_currency(value,currency)ที่ทำหน้าที่ในการแปลงสกุล
#THB <-> USD กำหนดให้ 1 USD = 33 THB

#ทั้งนี้ให้ function ดังกล่าว รับข้อมูล จำนวนเงินที่ต้องการแปลง และสกุลเงินปลายทาง
#ตัวอย่างวิธีการเรียกใช้
#convert_currency(100,"USD")
#convert_currency(100,"THB")

#ตัวอย่างหน้าจอ
#100 THB = 3.33 USD
#100 USD = 3300.0 THB

def convert_currency(value,currency):
    result = 0
    if currency == "USD":
        result = value / 33.0
        print(f"{value} THB = {result} USD")
    else:
        result = value * 33.0
        print(f"{value} USD = {result} THB")

    convert_currency(100,"USD")
    convert_currency(100,"THB")

