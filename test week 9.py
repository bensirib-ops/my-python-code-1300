try:
    num1 = float(input("ตัวเลขที่ 1:"))
    num2 = float(input("ตัวเลขที่ 2:"))
    operator = input("เครื่อง(+,-,*,/):")
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมาย + - * / เท่านั้น")

    print(f"{num1} {operator} {num2} = {result}")
except ValueError:
    print("กรุณากรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

else:
    print("ทำงานได้สมบูรณ์")