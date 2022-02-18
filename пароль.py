pass1 = input("введите пароль: ")
pass2 = input("введите пароль: ")

if (len(pass1)) < 8:
    print("короткий!")

elif pass1.find("123") != -1:
    print("простой!")
    
elif pass1 != pass2:
    print("различается!")
    
else:
    print("OK")




