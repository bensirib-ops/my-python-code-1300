def calculate_circle_area(radius):
    """Calculates and displays circle area"""
    area = radius**2
    print(f"circle with length {radius} and width {width}")
    print(f"Area = {radius} × {width} = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5, 3) #กลับไปรันบรรทัดที่ def calculate_rectangle_area(length, width):
calculate_circle_area(10, 7)
def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    if premium == True:
        return f"{username} (age:{age}) - premium user"
    else:
        return f"{username} (age:{age}) - standard user"

print(create_user_profile("Cello",19))
print(create_user_profile("Mana"))
print(create_user_profile("Piti",23,True))