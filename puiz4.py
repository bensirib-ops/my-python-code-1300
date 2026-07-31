#รับข้อมูล "ชื่อจริง (เป็นภาษาอังกฤษ)" จากผู้ใช้
#นับจำนวนสระในจข้อความดังกล่าว

#ตัวอย่างหน้าจอ 
#what's your name?: 
#you have 4 vowels in your text.
#name = input("What's your name?:")
name = input("What is your name?:")
letters = list(name)
counter = 0

for char in letters:
    if char == 'a' or char == 'A':
        counter = counter + 1

    elif char == 'e' or char == 'E':
        counter = counter + 1

    elif char == 'i' or char == 'I':
        counter = counter + 1

    elif char == 'o' or char == 'O':
        counter = counter + 1

    elif char == 'u' or char == 'U':
        counter = counter + 1

#ท่าที่ 2
a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

vowels = a + e + i + o + u 

print("You have", counter,"vowels in your text.")
print(f"you have {vowels} vowels in your text.")