#เขียนโปรแกรมตรวจสอบความแข็งแรงของ passsowrd
#password ที่แข็งแรงคือ ยาวมากกว่า 8 ตัว และผสมกันระหว่างตัวเลข ตัวอักษร และอักขระพิเศษ

#ตัวอย่างหน้าจอ
#insert your password:123;
#your password is not not sreong!

password = input("Insert your password")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:
    print("Your password is strong!")
else:
    print("Your password is not strong!")

#insert your password:1234;
#your password is strong