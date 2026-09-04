#เขียนโปรแกรมนับจำนวนอักขระที่สนใจในข้อความที่กำหนดโดยผู้ใช้
#1 มีการรับข้อความที่กำหนดจากผู้ใช้
#2 รับอักขระที่สนใจจากผู้ใช้
#3 แสดงผลการนับอักขระที่สนใจในข้อความออกทางหน้า

# ตัวอย่างจากตัวอย่าง
#insert the text : kasetsetsart Srirscha
#Character to find 'r'
# 3 letters 'r' found in 'ksetsart sriracha'


print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert the text:")#รับข้อมูลข้อความจากผู้ใช้
char = input("Character to find:")#รับข้อมูลตรวจสอบตัวอักษรจากผู้ใช้
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

