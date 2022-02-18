login_ = input ("введите логин: ")

mail_ = input ("введите почту: ")

if login_.find("@") == -1 and mail_.find("@mail.ru") != -1:
    print ("OK")
else:
    print ("логин или почта неверны")

